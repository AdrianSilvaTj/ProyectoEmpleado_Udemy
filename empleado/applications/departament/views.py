from django.shortcuts import render
from .models import Departament
from django.views.generic import ListView, DetailView

class DepartamentListView(ListView):
    template_name = "departament/list-all.html"
    
    def get_queryset(self):
        return Departament.objects.all()
    
class DepartamentDetailView(DetailView):
    model = Departament
    template_name = "departament/details.html"

    

