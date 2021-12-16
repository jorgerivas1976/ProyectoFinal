from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Bibliotecas)

admin.site.register(Libros)

admin.site.register(Asociados)