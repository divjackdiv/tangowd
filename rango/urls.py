from django.conf.urls import patterns,include,url
from rango import views

urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/$', views.account, name='account'),
    url(r'^trustworthybank/$', views.bienvenue, name='bienvenue'),
    url(r'^trustworthybank/emessage$', views.emessage, name='emessage'),
)
=======
    url(r'^accounts/', include('registration.backends.simple.urls')), 
    url(r'^$', views.bienvenue, name='bienvenue'),
)
>>>>>>> eb71a171e7603838f9a32f4513a662b7e0da5efc
