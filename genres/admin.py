from django.contrib import admin
from genres.models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
