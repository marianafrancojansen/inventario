from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'principal.views.index'),
    url(r'^map/$', 'map.views.index'),

    url(r'^admin/', include(admin.site.urls)),
)
