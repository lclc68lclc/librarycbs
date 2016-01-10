from django.conf.urls import patterns, url
from libraryinv import views

urlpatterns = patterns('',
                       url(r'^$',views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^add_title/$', views.add_title, name='add_title'),
                       url(r'^add_publisher/$', views.add_publisher, name='add_publisher'),
                       )