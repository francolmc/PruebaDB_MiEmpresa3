from django.contrib import admin
from .models import Categoria, Tecnologia, Proyecto, Etiquetas

# Register your models here.
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')
    list_filter = ('categoria', 'tecnologias', 'etiquetas')
    search_fields = ('titulo', 'descripcion')

admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Etiquetas)
admin.site.register(Proyecto, ProyectoAdmin)