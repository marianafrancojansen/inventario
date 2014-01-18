from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'principal.views.index'),
    url(r'^principal/$', 'principal.views.index'),
    url(r'^map/$', 'map.views.index'),
    url(r'^fundadores/$', 'fundadores.views.index'),
    url(r'^noticias/$', 'noticias.views.index'),
    url(r'^vision/$', 'vision.views.index'),
    url(r'^proceso/$', 'proceso.views.index'),
    url(r'^contacto/$', 'contacto.views.index'),
    url(r'^inventarios/$', 'inventarios.views.index'),
    url(r'^lideres/$', 'lideres.views.index'),
    url(r'^vacantes/$', 'vacantes.views.index'),
    url(r'contacto/gracias/$', 'contacto.views.gracias'),
   

    url(r'^admin/', include(admin.site.urls)),
)
