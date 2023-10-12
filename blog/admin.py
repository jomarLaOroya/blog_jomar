from django.contrib import admin
from blog.models import *

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion',)

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'apellidos', 'estado', 'fecha_creacion',)

class PostAdmin(admin.ModelAdmin):
    search_fiels = ['titulo']
    list_display = ('titulo', 'descripcion', 'autor', 'estado', 'fecha_creacion',)
# Register your models here.

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
