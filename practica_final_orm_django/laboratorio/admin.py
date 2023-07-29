from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.


class LaboratorioAdmin(admin.ModelAdmin):
    search_fields = "nombre"
    list_display = ("id", "nombre")


admin.site.register(Laboratorio, LaboratorioAdmin)

admin.site.register(DirectorGeneral)

admin.site.register(Producto)
