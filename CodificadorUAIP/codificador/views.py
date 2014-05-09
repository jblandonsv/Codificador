# -*- coding: utf-8 -*-
import json
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from codificador.forms import LoginForm, ArchivoForm,FoliosFormset

from codificador.models import Archivo, folio, Serie, Tipo, TipoInformacion, TipoVigencia,UnidadesPermitidas

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.conf import settings

def entrar(request):
	print 'entro'
	if request.user.is_authenticated():
		return HttpResponseRedirect('inicio')
	if request.method == 'POST':
		print 'esta haciendo post'
		#siguiente = request.GET.get('next')
		#print 'valor de next = ' + str(siguiente)
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			usuario = authenticate(username=username,password=password)
			if usuario is not None:
				login(request,usuario)
				context = {'prueba':'mensaje','URL_STATICOS':settings.URL_STATICOS}
				#return render_to_response('alcaldias/principal.html',context,context_instance=RequestContext(request))
				return HttpResponseRedirect('inicio')
			else:
				form = LoginForm()
				return  render_to_response('codificador/login.html',{'form':form,'message':'Usuario o Password Incorrectos','URL_STATICOS':settings.URL_STATICOS},context_instance=RequestContext(request)) 
		else:
			return render_to_response('codificador/login.html',{'form':form,'URL_STATICOS':settings.URL_STATICOS},context_instance=RequestContext(request))
	else:
		form = LoginForm()
		context = {'form':form,'URL_STATICOS':settings.URL_STATICOS}
		return render_to_response('codificador/login.html',context,context_instance=RequestContext(request))

#Vistas para uso de catalogos
def obtener_tipos(request,serie_id):
	tipos = Tipo.objects.filter(serie__id = serie_id)
	data = list()
	for tipo in tipos:
		dato = {'id_tipo':tipo.id,'nombre_tipo':tipo.nombre}
		data.append(dato)
	
	response = HttpResponse(json.dumps({'tipos':data}),content_type="application/json; charset=utf8")
	return response

def obtener_series(request):
	series = Serie.objects.all()
	data = list()
	for serie in series:
		dato = {'id_serie':serie.id,'nombre_serie':serie.nombre}
		data.append(dato)
	
	response = HttpResponse(json.dumps({'series':data}),content_type="application/json; charset=utf8")
	return response

@login_required(login_url='entrar')
def archivos_usuario(request):
	usuario = request.user.username
	archivos_permitidos = None
	unidades_permitidas = list()
	data = list()
	#TODO - Filtrar listado de archivos en base a las unidades que tiene permisos un usuario
	if request.user.is_superuser:
		#Si es un super usuario, podra ver todos los archivos
		archivos_permitidos = Archivo.objects.all()
	else:
		#Si NO es super usuario, se filtararan los archivos en base a las unidades permitidas
		unidades = UnidadesPermitidas.objects.filter(user = request.user)
		for unidad in unidades:
			unidades_permitidas.append(unidad.unidades)
		archivos_permitidos = Archivo.objects.filter(unidad_responsable__in=unidades_permitidas)

	for archivo in archivos_permitidos:
		#print archivo.tipo.nombre
		data.append({'nombre':archivo.nombre,
			'dependencia':archivo.dependencia.nombre,
			'unidad_responsable':archivo.unidad_responsable.nombre,
			'serie':archivo.serie.nombre,
			#'tipo':archivo.tipo.nombre,
			'descripcion':archivo.descripcion,
			'unidades_bajo_codigo':archivo.unidades_bajo_codigo,
			'fecha_actualizacion':str(archivo.fecha_actualizacion),
			'codigo_referencia':archivo.codigo_referencia,
			'codigo':archivo.codigo})

	response = HttpResponse(json.dumps({'usuario':usuario,'archivos':data}),content_type="application/json; charset=utf8")

	return response

class ArchivoCreateView(CreateView):
	template_name = 'archivo/archivo_add.html'
	model = Archivo
	form_class = ArchivoForm
	success_url = 'exito/'

	def get(self, request, *args, **kwargs):
		"""
		Handles GET requests and instantiates blank versions of the form
		and its inline formsets.
		"""
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		folio_form = FoliosFormset()
		#instruction_form = InstructionFormSet()
		return self.render_to_response(
			self.get_context_data(form=form,
									folio_form=folio_form,))
									#instruction_form=instruction_form))

	def post(self, request, *args, **kwargs):
		"""
		Handles POST requests, instantiating a form instance and its inline
		formsets with the passed POST variables and then checking them for
		validity.
		"""
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		folio_form = FoliosFormset(self.request.POST)
		if (form.is_valid() and folio_form.is_valid()):
			return self.form_valid(form, folio_form,)
		else:
			return self.form_invalid(form, folio_form,)

	def form_valid(self, form, folio_form):
		"""
		Called if all forms are valid. Creates a Recipe instance along with
		associated Ingredients and Instructions and then redirects to a
		success page.
		"""
		self.object = form.save()
		ingredient_form.instance = self.object
		ingredient_form.save()
	 	instruction_form.instance = self.object
		instruction_form.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, folio_form):
		"""
		Called if a form is invalid. Re-renders the context data with the
		data-filled forms and errors.
		"""
		return self.render_to_response(
		self.get_context_data(form=form,
								folio_form=folio_form,))