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
    num_visitas = request.session.get("num_visits", 1)
    request.session["num_visits"] = num_visitas + 1
    context = {
        "laboratorios": laboratorios,
        "num_visitas": num_visitas,
    }
    return render(request, "laboratorio/mostrar.html", context)


def editar_lab_view(request, pk):
    if request.method == "POST":
        form = LaboratorioForm(request.POST)
        print(request.POST)
        if form.is_valid():
            laboratorio = Laboratorio.objects.get(id=pk)
            laboratorio.lab_id = request.POST["lab_id"]
            laboratorio.nombre = request.POST["nombre"]
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
