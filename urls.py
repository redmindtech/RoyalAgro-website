"""royalAgro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
import django.views.static as django_static_view
from django.views.generic import TemplateView

from royalAgro_app.views import *

urlpatterns = [
    url(r'^$', index, name='index'),

    
    url(r'^google09ea22e392feb889$',TemplateView.as_view(template_name="google09ea22e392feb889.html", content_type="text/html")),
    url(r'^sitemap.xml$',TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")),
    url(r'^humans.txt$',TemplateView.as_view(template_name="humans.txt")),
    url(r'^robots.txt$',TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    
    url(r'^about/$', about, name='about'),
    url(r'^commodities/$', commodities, name='commodities'),
    url(r'^resources/$', resources, name='resources'),
    url(r'^news/$', news, name='news'),
    url(r'^gallery/$', gallery, name='gallery'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^contact/confirmation/$', contact_confirmation, name='contact_confirmation'),
    
    url(r'^peanuts/$', peanuts, name='peanuts'),
    url(r'^greenmungbean/$', greenmungbean, name='greenmungbean'),
    url(r'^coriander/$', coriander, name='coriander'),
    url(r'^chillies/$', chillies, name='chillies'),
    url(r'^soybeans/$', soybeans, name='soybeans'),
    url(r'^corn/$', corn, name='corn'),
    url(r'^privacy/$', privacy, name='privacy'),
    url(r'^terms/$', terms, name='terms'),
    

    # Media URL's
    url(r'^site_media/(?P<path>.*)$', django_static_view.serve, {'document_root': settings.MEDIA_ROOT }),
    url(r'^static/admin/(?P<path>.*)$', django_static_view.serve, {'document_root': settings.STATIC_ROOT }),
]
