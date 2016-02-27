from django.conf.urls import patterns,include,url
from rango import views
from random import randint

import re

urlpatterns = patterns('',
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/$', views.account, name='account'),
    url(r'^trustworthybank-5672/$', views.bienvenue, name='bienvenue'),
    url(r'^trustworthybank/emessage$', views.emessage, name='emessage'),
)

many = 9999
for i in range(many):
    url_string = r'^trustworthybank-' + re.escape(str(i))
    urlpatterns += url(url_string, views.bienvenue_fake, name='bienvenue_fake' + str(i)),
