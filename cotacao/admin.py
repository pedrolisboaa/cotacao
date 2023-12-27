from django.contrib import admin
from .models import Moeda

# Register your models here.

@admin.register(Moeda)
class MoedasAdmin(admin.ModelAdmin):
    list_display = 'id', 'sigla', 'moeda', 'bandeira',
