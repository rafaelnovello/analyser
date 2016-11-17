from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.detail, name='document-detail'),
    url(r'^add/$', views.create, name='document-create'),
    url(r'^(?P<id>\d+)/groupby/(?P<col>[-\w]+)/$', views.groupby, name='groupby'),
    url(r'^(?P<id>\d+)/numstats/$', views.numstats, name='numstats'),
]
