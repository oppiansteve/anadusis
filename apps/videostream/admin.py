# -*- coding: utf-8 -*-

# © Copyright 2009 Andre Engelbrecht. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence

from django.contrib import admin
from videostream.models import VideoStream

class VideoStreamAdmin(admin.ModelAdmin):
    fieldsets = [
            ('General', {'fields': ['title', 'description']}),
            ('Publication', {'fields': ['author', 'tags', 'is_public', 'featured', 'enable_comments']}),
            ('Video Files', {'fields': ['videoupload', 'flvfile', 'thumbnail']}),
            ('Encoding Options', {'fields': ['encode']}),
            ]
    date_hierarchy = 'date_added'
    list_display = ['title', 'flvfile', 'date_added', 'is_public', 'featured', 'enable_comments', 'encode']
    list_filter = ['date_added', 'is_public', 'featured','enable_comments',  'encode']
    search_fields = ['title', 'description', 'tags']

admin.site.register(VideoStream, VideoStreamAdmin)
