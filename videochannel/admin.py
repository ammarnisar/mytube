# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Video ,Likes ,Comment ,Channel,Profile


# Register your models here.

admin.site.register(Video)
admin.site.register(Likes)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Channel)