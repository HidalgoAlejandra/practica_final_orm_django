from django.urls import path

from . import views

urlpatterns = [
    path("", views.insertar_lab_view, name="insertar_lab"),
    path("mostrar/", views.mostrar_lab_view, name="mostrar_emp"),
    path("editar/<int:pk>/", views.editar_lab_view, name="editar_emp"),
    path("eliminar/<int:pk>/", views.eliminar_lab_view, name="eliminar_emp"),
]
