from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("insertar/", views.insertar_lab_view, name="insertar_lab"),
    path("mostrar/", views.mostrar_lab_view, name="mostrar_lab"),
    path("editar/<int:pk>/", views.editar_lab_view, name="editar_lab"),
    path("eliminar/<int:pk>/", views.eliminar_lab_view, name="eliminar_lab"),
    path(
        "laboratorio/<int:pk>/",
        views.laboratorio_detalle_view,
        name="laboratorio_detalle",
    ),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
]
