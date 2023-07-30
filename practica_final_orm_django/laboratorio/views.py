from django.shortcuts import render, redirect, HttpResponse
from .forms import LaboratorioForm
from .models import Laboratorio


# Create your views here.
def insertar_lab_view(request):
    if request.method == "POST":
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/laboratorio/mostrar/")
    form = LaboratorioForm()
    context = {"form": form}
    return render(request, "laboratorio/insertar.html", context)


def mostrar_lab_view(request):
    laboratorios = Laboratorio.objects.all()
    context = {
        "laboratorios": laboratorios,
    }
    return render(request, "laboratorio/mostrar.html", context)


def editar_lab_view(request, pk):
    if request.method == "POST":
        form = LaboratorioForm(request.POST)
        print(request.POST)
        if form.is_valid():
            laboratorio = Laboratorio.objects.get(id=pk)
            laboratorio.nombre = request.POST["nombre"]
            laboratorio.ciudad = request.POST["ciudad"]
            laboratorio.pais = request.POST["pais"]
            laboratorio.save()
            return redirect("/laboratorio/mostrar/")
    laboratorio = Laboratorio.objects.get(id=pk)
    form = LaboratorioForm(instance=laboratorio)
    context = {"form": form, "laboratorio": laboratorio}
    return render(request, "laboratorio/editar.html", context)


def eliminar_lab_view(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == "POST":
        laboratorio.delete()

        return redirect("/laboratorio/mostrar/")
    context = {"laboratorio": laboratorio}
    return render(request, "laboratorio/eliminar.html", context)


def laboratorio_detalle_view(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    context = {"laboratorio": laboratorio}
    return render(request, "laboratorio/detalle.html", context=context)
