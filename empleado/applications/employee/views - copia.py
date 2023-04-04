from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Employee


class EmployeeListView(ListView):
    model = Employee
    template_name = "employee/list-all.html"
    paginate_by = 5
    
class EmployeeListByAreaView(ListView):
    """Todos los empleados de un Area"""
    model = Employee
    template_name = "employee/list-by-area.html"
    
   
    def get_queryset(self):
        # Recoge la variable pasada por la url
        area = self.kwargs['shortname']
        queryset = Employee.objects.filter(departament__short_name=area)
        return queryset
        
class EmployeeListByKwordView(ListView):
    """Lista empleados por palabra clave"""
    model = Employee
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
        return self.employee.skills.all()
    
    #En 'context' se guarda primero los datos de queryset y luego se le agrega el nombre del employee
    def get_context_data(self, **kwargs):
        context = super(EmployeeSkillsView, self).get_context_data(**kwargs)
        context['employee'] = self.employee
        return context
    

class EmployeeDetailView(EmployeeSkillsView):
    template_name = "employee/employee-detail.html"
    
