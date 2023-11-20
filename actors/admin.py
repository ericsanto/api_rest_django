from django.contrib import admin
from actors.models import *


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality', 'birthday')
