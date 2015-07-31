from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^new$', views.CaptureCreate.as_view(), name='capture-new'),
                       url(r'^list$', views.CaptureList.as_view(), name='capture-list')
                       )
