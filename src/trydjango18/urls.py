#!/usr/bin/env python
#**********************************************************************#
# File Name: urls.py
# Writen By: Ashish Kapoor
# Project Name: Activity for Zenatix
# Purpose of this file: Source of all the Routes
#**********************************************************************#

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'msg.views.home', name='home'),
    url(r'^contact/$', 'msg.views.contact', name='contact'),
    url(r'^about/$', 'msg.views.about', name='about'),
    url(r'^allMsgs/$', 'msg.views.allMsgs', name='allMsgs'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
