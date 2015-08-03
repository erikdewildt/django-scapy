from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^files/add$', views.CaptureCreate.as_view(), name='capture-add'),
                       url(r'^files/$', views.CaptureList.as_view(), name='capture-list'),
                       url(r'^files/(?P<pk>\d+)/delete$', views.CaptureDelete.as_view(), name='capture-delete'),
                       url(r'^files/(?P<pk>\d+)/edit$', views.CaptureEdit.as_view(), name='capture-edit'),
                       url(r'^files/(?P<pk>\d+)$', views.CaptureDetail.as_view(), name='capture-detail'),
                       )
