from django.conf.urls import patterns, include, url
from django.contrib import admin

from captures import views # include temp homepage

urlpatterns = patterns('',
                       url(r'^$', views.CaptureList.as_view(), name='home'), # temp home page
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^captures/', include('captures.urls', namespace='captures')),
                       )
