from django.shortcuts import render
from.models import JhonatanSotelo
from.forms import CrearForm

# Create your views here.

from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView
# Create your views here.

class HomeView(TemplateView):
    template_name="home.html"

class CreateView(CreateView):
    model = JhonatanSotelo
    template_name= "crear.html"
    form_class = CrearForm
    success_url = "/crear"
    
class ListView(ListView):
    model = JhonatanSotelo
    template_name="listar.html"
    success_url = "/list"
    
class ActualizarListView(ListView):
    model = JhonatanSotelo
    template_name="actualizar.html"
    success_url = "/actualizar"
    
class UpdateView(UpdateView):
    model = JhonatanSotelo
    fields=[
        "finca",
        "hectareas",
        "metros2",
        "propietario",
        "cultivo"
    ]
    template_name="actualizarid.html"
    success_url = "/actualizar"

class EliminarListView(ListView):
    model = JhonatanSotelo
    template_name="eliminar.html"
    success_url = "/eliminar"
    
class DeleteView(DeleteView):
    model = JhonatanSotelo
    template_name="eliminarid.html"
    success_url="/eliminar"