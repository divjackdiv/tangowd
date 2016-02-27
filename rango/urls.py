from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^trustworthybank/', views.bienvenue, name='bienvenue'),
       )