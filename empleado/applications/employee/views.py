from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView,TemplateView

from .models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = "employee/list-all.html"
    paginate_by = 5
    
class EmployeeListByAreaView(ListView):
    """Todos los empleados de un Area"""
    template_name = "employee/list-by-area.html"
    
   
    def get_queryset(self):
        # Recoge la variable pasada por la url
        area = self.kwargs['shortname']
        queryset = Employee.objects.filter(departament__short_name=area)
        return queryset
        
class EmployeeListByKwordView(ListView):
    """Lista empleados por palabra clave"""
    template_name = "employee/list-by-kword.html"
    context_object_name = 'employeesList'
   
    def get_queryset(self):
        kword = self.request.GET.get('kword')
        queryset = Employee.objects.filter(first_name=kword)
        print (queryset)
        return queryset
    

class EmployeeSkillsView(ListView):
    template_name = "employee/employee-skills.html"
    employee = []
    
    # Se guardan los datos de la tabla 'skill' del employee buscado
    def get_queryset(self):
        id = self.kwargs['id']
        self.employee = Employee.objects.get(id=id)
        #print(self.employee)        
        return self.employee.skills.all()
    

class EmployeeDetailView(EmployeeSkillsView):
    template_name = "employee/employee-detail.html"    
    
    #En 'context' se guarda primero los datos de queryset y luego se le agrega el nombre del employee
    def get_context_data(self, **kwargs):
        context = super(EmployeeSkillsView, self).get_context_data(**kwargs)
        context['employee'] = self.employee
        return context
    
class EmployeeListByJobView(ListView):
    """Todos los empleados de un Trabajo"""
    template_name = "employee/list-by-job.html"
    strJob = ""
    error = ""    
   
    def get_queryset(self):
        # Recoge la variable pasada por la url
        numJob = self.kwargs['job']        
        queryset = Employee.objects.filter(job=numJob)
        if (queryset.count() == 0):
            self.error = "No existen Empleados con ese Trabajo"
        else:
            #Accede al primer elemento del queryset y le asigna la cadena del valor asociada al choice del job
            self.strJob =  queryset[0].get_job_display()
        return queryset        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega dos variables al contexto
        context["job"] = self.strJob
        context["error"] = self.error 
        return context
    
    
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employee/add.html"
    #fields = ('__all__')
    fields = [
        'first_name',
        'last_name', 
        'job',
        'departament',
        'skills',
        'cv'
    ]
    #success_url ='.' #Redirecciona al mismo url cuando se crea con exito
    success_url = reverse_lazy('employee:success')
    
    def form_valid(self, form):
        # copia todos los datos del form con sus campos, commit=False se utiliza para que no se guarde en la base de datos
        employee = form.save(commit=False)
        employee.full_name = employee.first_name + ' ' +employee.last_name
        employee.save()
        return super(EmployeeCreateView,self).form_valid(form)
    
class Success(TemplateView):
    template_name = "employee/success.html"
