from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .forms import LaboratorioForm
from .models import Laboratorio

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


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


def logout_view(request):
    logout(request)
    messages.info(request, "Seha cerrado la sesion satisfactoriamente.")
    return HttpResponseRedirect("/")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"iniciaste sesion como: {username}.")
                return HttpResponseRedirect("/laboratorio/mostrar")
            else:
                messages.error(request, "username o password Incorrectos")
                return HttpResponseRedirect("/laboratorio/login")
        else:
            messages.error(request, "username o password Incorrectos")
            return HttpResponseRedirect("/laboratorio/login")
    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "laboratorio/login.html", context)


def index(request):
    return render(request, "laboratorio/index.html")
