#!/usr/bin/env python
# -*- coding:utf8 -*-
# Copyright (C) 2012  FinalsClub Foundation

from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from django.views.generic.simple import direct_to_template

from karmaworld.apps.ajaxuploader.views import ajax_uploader
from karmaworld.apps.courses.models import Course
from karmaworld.apps.courses.views import AboutView
from karmaworld.apps.courses.views import CourseDetailView
from karmaworld.apps.notes.views import NoteView
from karmaworld.apps.notes.views import raw_file

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^terms/$', direct_to_template, { 'template': 'terms.html' }, name='terms'),

    url(r'^about/$', AboutView.as_view(), name='about'),

    url(r'^raw/(?P<pk>\d+)$', raw_file, name='note_raw'),
    url(r'^(?P<school_slug>[^/]+)/(?P<slug>[^/]+)$', \
        CourseDetailView.as_view(), name='course_detail'),

    # note file as id, for notes without titles yet
    url(r'^(?P<school_slug>[^/]+)/(?P<course_slug>[^/]+)/(?P<pk>[\d^/]+)$', \
        NoteView.as_view(), name='note_detail_pk'),
    # note file by note.slug
    url(r'^(?P<school_slug>[^/]+)/(?P<course_slug>[^/]+)/(?P<slug>[^/]+)$', \
        NoteView.as_view(), name='note_detail'),

    # uploading
    url(r'ajax-upload$', ajax_uploader, name='ajax_upload'),

    url(r'^$', ListView.as_view(model=Course), name='home'),
)
