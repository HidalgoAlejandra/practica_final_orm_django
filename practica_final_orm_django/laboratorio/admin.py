from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.


class LaboratorioAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]
    list_display = ["id", "nombre"]
    ordering = ["nombre"]


class DirectorGeneralAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]
    list_display = ["id", "nombre", "laboratorio"]
    ordering = ["nombre"]


class ProductoAdmin(admin.ModelAdmin):
    search_fields = ["nombre", "laboratorio"]
    list_display = [
        "id",
        "nombre",
        "laboratorio",
        "f_fabricacion",
        "p_costo",
        "p_venta",
    ]
    ordering = ["nombre"]
    list_filter = ("nombre", "laboratorio")


admin.site.register(Laboratorio, LaboratorioAdmin)

admin.site.register(DirectorGeneral, DirectorGeneralAdmin)

admin.site.register(Producto, ProductoAdmin)
