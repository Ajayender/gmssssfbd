# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from school.models import Slideshow,Latestnews,Album,Photos,Staff,Hof
from django.contrib import admin

# Register your models here.
admin.site.register(Slideshow)
admin.site.register(Latestnews)
admin.site.register(Album)
admin.site.register(Photos)
admin.site.register(Staff)
admin.site.register(Hof)
