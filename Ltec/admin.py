from django.contrib import admin
from .models import Encargado, Comentario, Supervisor, Administrador

#class ComentarioInline(admin.StackedInline):
#    model = Comentario

class ComentarioInline(admin.TabularInline):
    model = Comentario

class AdministradorAdmin(admin.ModelAdmin):
    inlines = [
        ComentarioInline
    ]
  

admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Supervisor)
admin.site.register(Encargado)
admin.site.register(Comentario)