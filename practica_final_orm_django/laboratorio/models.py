import datetime
from django.db import models


# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Laboratorio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Laboratorio"
        verbose_name_plural = "Laboratorios"

    def __str__(self):
        return self.nombre


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Director General")
    laboratorio = models.OneToOneField("Laboratorio", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actuialización"
    )

    class Meta:
        verbose_name = "DirectorGeneral"
        verbose_name_plural = "DirectoresGenerales"

    def __str__(self):
        return self.nombre


annos_choices = []

for r in range(1999, (datetime.datetime.now().year + 1)):
    annos_choices.append((r, r))


def anno_actual():
    return datetime.date.today().year


class Producto(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    laboratorio = models.ForeignKey(
        "Laboratorio", on_delete=models.SET_NULL, blank=True, null=True
    )
    f_fabricacion = models.IntegerField(
        choices=annos_choices, default=anno_actual, verbose_name="Fecha de Fabricacion"
    )
    # f_fabricacion = models.DateField(verbose_name="Fecha de Fabricacion")
    p_costo = models.DecimalField(
        null=False, decimal_places=2, max_digits=10, verbose_name="Precio de Costo"
    )
    p_venta = models.DecimalField(
        null=False, decimal_places=2, max_digits=10, verbose_name="Precio de Venta"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actuialización"
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
