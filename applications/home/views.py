from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'
    
class IndexView(TemplateView):
    template_name = 'home/home.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['A','B','C']
    context_object_name = 'lista_prueba'
    
class ModelPruebaListView(ListView):
    model = Prueba
    template_name = 'home/lista.html'
    #queryset = 
    context_object_name = 'lista_prueba'
    

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '.'

