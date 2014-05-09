from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from codificador import views
from codificador.views import *
urlpatterns = patterns('',
	#url(r'^$', views.inicio, name='inicio'),
	#url(r'^inicio$', views.inicio, name='inicio'),
	#url(r'^entrar$',views.entrar,name='entrar'),
	#url(r'^salir$',views.salir,name='salir'),
    url(r'^getTipos/(?P<serie_id>\d+)/$',views.obtener_tipos,name='getTipos'),
    url(r'^getSeries/$',views.obtener_series,name='getSeries'),
    url(r'^getArchivos/$',views.archivos_usuario,name='getArchivos'),
    url(r'^archivo/add/$',ArchivoCreateView.as_view(),name='archivos-add'),
    #url(r'^getAlcaldias$',views.getAlcaldias,name='getAlcaldias'),
    #url(r'^isRegistrada/(?P<idMunicipio>\d+)/$',views.isRegistrada,name='isRegistrada'),
    #url(r'^errorsocket$',views.socket_error,name=' socket_error'),
    #url(r'^navegadores$',views.navegadores,name=' navegadores'),
   
    # Examples:
    # url(r'^$', 'servicionacidosvivos.views.home', name='home'),
    # url(r'^servicionacidosvivos/', include('servicionacidosvivos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
