# -*- coding: utf-8 -*-
from django.contrib import admin
from codificador.models import Unidad, Serie, Tipo, Archivo, Dependencia, Correlativo,folio,TipoInformacion,ArchivoHistorico,FolioHistorico,TipoVigencia,EstadoExpediente,UnidadesPermitidas

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

import autocomplete_light

from codificador.forms import ArchivoForm

class TipoInline(admin.StackedInline):
	model = Tipo

class FolioInline(admin.StackedInline):
	model = folio
	classes = ['collapse', 'extrapretty']
	extra = 0
	verbose_name ="Expedientes"

class FolioHistoricoInline(admin.TabularInline):
	model = FolioHistorico
	readonly_fields = ['nombre','tipo_de_informacion','ubicacion','codigo','descripcion','fecha_creacion']
	extra = 0

	#classes = ('collapse',)
	#inline_classes = ('collapse',)

class CorrelativoAdmin(admin.ModelAdmin):
	list_display = ['dependencia','correlativo_actual','year']
	list_filter = ['dependencia','year']


class HistoricoAdmin(admin.ModelAdmin):
	readonly_fields = ['archivo','nombre','dependencia','unidad_responsable','serie','tipo','descripcion','codigo','reference_descriptivo','fecha','comentario']
	search_fields = ['codigo','nombre','fecha']
	list_display = ['codigo','comentario','fecha']
	list_filter = ['codigo','dependencia']
	inlines = [FolioHistoricoInline]

class FolioAdmin(admin.ModelAdmin):
	list_display = ['archivo','codigo','nombre','tipo_de_informacion']
	list_filter = ['tipo_de_informacion','estado','tipo_vigencia']
	search_fields = ['codigo','nombre']
	verbose_name = "Expedientes"

class ArchivoAdmin(admin.ModelAdmin):
	exclude = ('dependencia',)
	readonly_fields=('codigo','correlativo_sistema',)
	search_fields = ['codigo','nombre']
	list_filter = ['dependencia','serie','unidad_responsable']
	list_display = ['codigo','nombre','unidad_responsable','dependencia']
	class Media:
		js = ('/static/admin/js/dependant_autocomplete.js',)
	#form = autocomplete_light.modelform_factory(Archivo)
	form = ArchivoForm
	inlines = (FolioInline,)
	#inline_classes = ('collapse',)


class UnidadAdmin(admin.ModelAdmin):
	list_display = ['prefijo','nombre','unidad_superior','dependencia','abreviatura']
	readonly_fields=('reference','reference_descriptivo',)
	search_fields = ['nombre','prefijo']
	list_filter = ['dependencia']
	
	form = autocomplete_light.modelform_factory(Unidad)

	class Media:
		js = ('/static/admin/js/dependant_autocomplete.js',)
	#inlines = [SlidesInline]

class DependenciaAdmin(admin.ModelAdmin):
	list_display = ['nombre','abreviatura']
	search_fields = ['nombre','abreviatura']

class SerieAdmin(admin.ModelAdmin):
	list_display = ['prefijo','nombre']
	search_fields = ['nombre']
	list_filter = ['nombre']
	inlines = [TipoInline]

class UnidadesPermitidasInline(admin.StackedInline):
	extra = 0
	model = UnidadesPermitidas
	can_delete = False
	verbose_name_plural = "Unidades Permitida"

class UserAdmin(UserAdmin):
	inlines = (UnidadesPermitidasInline,)

class TipoAdmin(admin.ModelAdmin):
	list_display = ['nombre','prefijo']
	search_fields = ['nombre','prefijo','serie__nombre']
	list_filter = ['serie']

admin.site.register(Unidad,UnidadAdmin)
admin.site.register(Serie,SerieAdmin)
admin.site.register(Tipo,TipoAdmin)
admin.site.register(Archivo,ArchivoAdmin)
admin.site.register(Dependencia,DependenciaAdmin)
admin.site.register(Correlativo,CorrelativoAdmin)
admin.site.register(TipoInformacion)
admin.site.register(folio,FolioAdmin)
admin.site.register(ArchivoHistorico,HistoricoAdmin)
admin.site.register(EstadoExpediente)
admin.site.register(TipoVigencia)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(UnidadesPermitidas)