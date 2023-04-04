from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import NewDepartamentForm
from .models import Departament
from applications.employee.models import Employee
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

class DepartamentListView(ListView):
    template_name = "departament/list-all.html"
    paginate_by = 5
    
    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        queryset = Departament.objects.filter(name__icontains=kword)
        print (queryset)
        return queryset
    
class DepartamentDetailView(DetailView):
    model = Departament
    template_name = "departament/details.html"

class NewDepartamentView(FormView):
    template_name = 'departament/new_departament.html'
    form_class = NewDepartamentForm
    success_url = reverse_lazy('employee:success')
    
    def form_valid(self, form):
        departament = form.cleaned_data['departament']
        short_name = form.cleaned_data['short_name']
        depa = Departament.objects.create(
            name = departament,
            short_name = short_name,            
        )
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        Employee.objects.create(
            first_name = first_name,
            last_name = last_name,
            job = '1',
            departament = depa,
        )
        
        return super(NewDepartamentView,self).form_valid(form)
    

