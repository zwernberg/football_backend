# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from season.models import Season, Division

# Register your models here.

class SeasonAdmin(admin.ModelAdmin):
    pass

class DivisionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Season, SeasonAdmin)
admin.site.register(Division, DivisionAdmin)