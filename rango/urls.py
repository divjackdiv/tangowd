from django.conf.urls import patterns,include,url
from rango import views

urlpatterns = patterns('',
    url(r'^accounts/', include('registration.backends.simple.urls')), 
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^trustworthybank/', views.bienvenue, name='bienvenue'),
)