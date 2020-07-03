from django.contrib import admin
from .models import *


class AdminServerIP(admin.TabularInline):
    model = ServerIP
    extra = 1


class ServerChild(admin.TabularInline):
    model = Server
    extra = 1


@admin.register(Server)
class AdminServer(admin.ModelAdmin):
    list_display = ['name', 'create_dt', 'server_type']
    inlines = [
        AdminServerIP,
        ServerChild,
    ]
