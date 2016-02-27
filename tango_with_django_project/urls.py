from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import views

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^account/$', views.account, name='account'),
    url(r'^trustworthybank-6969/', include(admin.site.urls)),
    url(r'',include('rango.urls')),

)
