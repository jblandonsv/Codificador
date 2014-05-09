# -*- coding: utf-8 -*-
from django.db import models

from smart_selects.db_fields import ChainedForeignKey,GroupedForeignKey

from django.contrib.auth.models import User

import datetime 


class Dependencia(models.Model):
	prefijo = models.CharField(blank=False,max_length=10)
	nombre = models.CharField(blank=False,max_length=250)
	abreviatura = models.CharField(blank=False,max_length=10)

	def __unicode__(self):
		return self.nombre

	#def save(self,*args,**kwargs):
	#TODO - Actualizar archivos

class Correlativo(models.Model):
	dependencia = models.ForeignKey(Dependencia)
	correlativo_actual = models.IntegerField(blank = False)
	year = models.IntegerField(blank = False)

	def __unicode__(self):
		return self.dependencia.nombre

class Unidad(models.Model):
	prefijo = models.CharField(blank=False,max_length=5)
	nombre = models.CharField(blank=False,max_length=250)
	abreviatura = models.CharField(blank=True,max_length=10)
	dependencia = models.ForeignKey(Dependencia)
	unidad_superior=models.ForeignKey('self', null=True, blank=True)
	reference = models.CharField(blank=True,max_length=300)
	reference_descriptivo = models.TextField(blank=True)

	def __unicode__(self):
		return self.nombre

	def save(self,*args,**kwargs):
		#TODO: Modificacion, actualizar datos de archivos relacionados.
		if not self.unidad_superior==None:
			#Tiene una unidad superior
			self.reference = self.unidad_superior.reference + self.prefijo
			self.reference_descriptivo = self.unidad_superior.reference_descriptivo + ' > ' + self.nombre
		else:
			#No tiene Unidad Superior
			self.reference = self.prefijo
			self.reference_descriptivo = self.nombre

		#if not self.reference_descriptivo == None:
			#No es una unidad nueva por lo tanto hay una modificacion y debera actualizar los
			#Archivos. Primero se localizan esos archivos.

		#	archivos = Archivo.objects.filter(unidad_responsable = self)

			# Luego los datos anteriores de la unidad responsable
		#	unidad_anterior = Unidad.objects.filter(id = self.id)

		#	for arc in archivos:
		#		arc.unidad_responsable = self
		#		arc.save('Actualizacion de Unidad Responsable')

			# En este caso se modifican los archivos de la unidad especifica si se desea actualizar
			# los archivos de las unidades dependientes de esa unidad, se recomienda que vayan
			# modificando de unidada  unidad para que los ajustes tomen los cambios a nivel de archivo

			# Ejemplo: unidad administrativa. ITIGES - egob - desarrollo
			# Si se modifica ITIGES entonces solo los archivos de codigo ITIGEs son modificados
			# pero no  asi los de egob y desarrollo, para que estos se modifiquen se tendra que meter
			# a esas unidades y modificar cada una de ellas
		
		super(Unidad,self).save(*args,**kwargs)
		

class Serie(models.Model):
	prefijo = models.CharField(blank=False,max_length=5)
	nombre = models.CharField(blank=False,max_length=250)

	def __unicode__(self):
		return self.nombre

class Tipo(models.Model):
	prefijo = models.CharField(blank=False,max_length=5)
	nombre = models.CharField(blank=False,max_length=250)
	serie = models.ForeignKey(Serie)

	def __unicode__(self):
		return self.nombre


class Archivo(models.Model):
	nombre = models.CharField(max_length=300,blank=False)
	dependencia = models.ForeignKey(Dependencia)
	unidad_responsable = models.ForeignKey(Unidad, help_text = "escribir nombre o abreviatura de la unidad responsable del archivo")
	serie = models.ForeignKey(Serie)
	tipo = ChainedForeignKey(Tipo,blank=True,null=True,chained_field="serie",chained_model_field="serie",show_all=False,auto_choose=True)
	#tipo2 = ChainedForeignKey(Tipo,blank=True,chained_field="serie",chained_model_field="serie",show_all=False,auto_choose=True)
	descripcion = models.TextField(blank=True, max_length=600)
	unidades_bajo_codigo = models.IntegerField(blank = True,default = 1,help_text = "Numero de unidades identificadas con este codigo")
	fecha_actualizacion = models.DateField(blank = True, help_text = "Fecha en la cual se contabilizaron las unidades bajo este mismo Codigo CAI")
	codigo_referencia = models.CharField(max_length=300,blank = True, help_text ="Estructura del codigo interno con el que se identifica este codigo CAI.") 
	codigo = models.CharField(max_length=300, help_text = "Codigo CAI")
	correlativo_sistema = models.CharField(max_length=300)
	
	def __unicode__(self):
		return self.nombre

	def tipo_nombre(self):
		nombre = Tipo.objects.filter(id=self.tipo)[0].nombre
		return nombre

	def save(self,*args,**kwargs): 
		#self.tipo=Tipo()
		#print 'Esta intentando guardar algo'
		# TODO: Enviar al historico de Archivo en caso de una actualizacion
		if self.codigo == None or self.codigo == '':
			#Verificando si ya tenia codigo el archivo, si ya tiene entonces es actualizacion
			#se debe enviar al historico. En caso no tenga entonces se debe crear

			#HOT FIX 25/03/2014, para permitir valores nulos en el tipo
			
			if not self.tipo == None:
				codigo_nuevo = self.unidad_responsable.dependencia.prefijo + self.unidad_responsable.reference+'-'+self.serie.prefijo+'.'+self.tipo.prefijo
			else:
				codigo_nuevo = self.unidad_responsable.dependencia.prefijo + self.unidad_responsable.reference+'-'+self.serie.prefijo

			self.codigo = codigo_nuevo
			self.dependencia = self.unidad_responsable.dependencia
		else:
			# Ya tenia codigo, hay que enviar a historico antes de guardar la actualizacion
			anterior = Archivo.objects.filter(id = self.id)
			historico = ArchivoHistorico()
			historico.archivo = anterior[0]
			historico.nombre = anterior[0].nombre
			historico.dependencia = anterior[0].unidad_responsable.dependencia.nombre
			historico.unidad_responsable = anterior[0].unidad_responsable.nombre
			historico.serie = anterior[0].serie.nombre
			
			#HOT FIX 25/03/2014, para permitir valores nulos en el tipo

			if not anterior[0].tipo == None:
				historico.tipo = anterior[0].tipo.nombre
			else:
				historico.tipo = 'SIN TIPO'
			
			historico.descripcion = anterior[0].descripcion
			historico.codigo = anterior[0].codigo
			historico.reference_descriptivo = anterior[0].unidad_responsable.reference_descriptivo
			historico.fecha = datetime.datetime.now()
			#if not args[0] == None:
			historico.comentario = 'Actualizacion de archivo, ya sea datos generales o folios'
			#else:
			#	historico.comentario = str(args[0])

			#Guardando Historico (Dato General del Archivo)
			historico.save()

			#Guardando Informacion de los Folios
			folios_antes = folio.objects.filter(archivo = self)
			for folio_anterior in folios_antes:
				fa = FolioHistorico()
				fa.archivo_historico = historico
				fa.nombre = folio_anterior.nombre
				fa.tipo_de_informacion = folio_anterior.tipo_de_informacion
				fa.ubicacion = folio_anterior.ubicacion
				fa.codigo = folio_anterior.codigo
				fa.descripcion = folio_anterior.descripcion
				fa.fecha_creacion = folio_anterior.fecha_creacion
				fa.save()

		#Guardando cambios
		try:
			print 'algo esta intentando'
			super(Archivo,self).save(*args,**kwargs)
		except Exception:
			raise

	#YA NO SERA NECESARIO UTILIZAR EL CORRELATIVO
	#def save(self,*args,**kwargs):
		
		#year = datetime.datetime.now().year

		#correlativo = Correlativo.objects.filter(dependencia=self.unidad_responsable.dependencia,year = year)
		#correlativo_nuevo = 0

		#if correlativo:
		#	correlativo_nuevo = correlativo[0].correlativo_actual + 1
		#	self.correlativo_sistema = str(correlativo_nuevo) + '-' + str(year)
		#else:
		#	print 'LOG - codificador UAIP: correlativo_actual No encontrado'

		#self.dependencia = self.unidad_responsable.dependencia
		#codigo_nuevo = self.dependencia.prefijo + self.unidad_responsable.reference+'-'+self.serie.prefijo+'.'+self.tipo.prefijo
		#self.codigo = codigo_nuevo

		#try:
		#	super(Archivo,self).save(*args,**kwargs)
		#	correlativo[0].correlativo_actual = correlativo_nuevo
		#	correlativo[0].save()
		#except Exception:
		#	raise

class ArchivoHistorico(models.Model):
	archivo = models.ForeignKey(Archivo)
	nombre = models.CharField(max_length=300,blank=False)
	dependencia = models.CharField(max_length=300,blank=False)
	unidad_responsable = models.CharField(max_length=300,blank=False)
	serie = models.CharField(max_length=300,blank=False)
	tipo = models.CharField(max_length=300,blank=True)
	descripcion = models.TextField(blank=True, max_length=600)
	codigo = models.CharField(max_length=300)
	reference_descriptivo = models.TextField(blank=True)
	comentario = models.CharField(max_length=300,blank=True)
	fecha = models.DateField(blank  = True)
	#correlativo_sistema = models.CharField(max_length=300)

class FolioHistorico(models.Model):
	archivo_historico = models.ForeignKey(ArchivoHistorico)
	nombre = models.CharField(max_length=300,blank=True)
	tipo_de_informacion = models.CharField(max_length=300,blank=True)
	ubicacion = models.CharField(max_length=300,blank=True)
	codigo = models.CharField(max_length=300,blank=True)
	descripcion = models.TextField(blank=True, max_length=600)
	fecha_creacion = models.DateField(blank = True)

class TipoInformacion(models.Model):
	nombre = models.CharField(max_length=300,blank=True)

	def __unicode__(self):
		return self.nombre

class EstadoExpediente(models.Model):
	nombre = models.CharField(max_length=300)

	def __unicode__(self):
		return self.nombre

class TipoVigencia(models.Model):
	nombre = models.CharField(max_length=300)

	def __unicode__(self):
		return self.nombre

class folio(models.Model):
	archivo = models.ForeignKey(Archivo)
	nombre = models.CharField(max_length=300,blank=True)
	tipo_de_informacion = models.ForeignKey(TipoInformacion, blank = True)
	ubicacion = models.CharField(max_length=300,blank=True)
	codigo = models.CharField(max_length=300,blank=True)
	descripcion = models.TextField(blank=True, max_length=600)
	estado = models.ForeignKey(EstadoExpediente,blank=True)
	vigencia = models.IntegerField(blank = True,default=0)
	tipo_vigencia = models.ForeignKey(TipoVigencia,blank=True)
	cantidad_paginas = models.IntegerField(blank=True, default=0)
	fecha_creacion = models.DateField(blank = True, help_text = "Fecha en la cual se contabilizaron las unidades bajo este mismo Codigo CAI")
	digital = models.BooleanField(blank = True, help_text = "Marcar en caso el documento se encuentre en formato digital")
	fisico = models.BooleanField(blank = True, help_text = "Marcar en caso el documento se encuentre en formato fisico")

	def __unicode__(self):
		return self.nombre

#Clase para identifica las unidades que un usuario tendra acceso
class UnidadesPermitidas(models.Model):
	user = models.ForeignKey(User)
	unidades = models.ForeignKey(Unidad)

	def __unicode__(self):
		return self.unidades.nombre + '('+self.unidades.dependencia.nombre+')'
