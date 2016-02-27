from django.conf.urls import patterns,include,url
from rango import views

urlpatterns = patterns('',
    url(r'^accounts/', include('registration.backends.simple.urls')), 
    url(r'^accounts/account/', views.account, name='account'),
    url(r'^trustworthybank/', views.bienvenue, name='bienvenue'),
)