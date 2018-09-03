# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from chat.models import ChatMessage

# Register your models here.

class ChatMessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(ChatMessage, ChatMessageAdmin)
