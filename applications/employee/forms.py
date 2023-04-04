from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = (
            'first_name',
            'last_name',
            'job',
            'departament',
            'picture',
            'skills',            
            )
        # Cambia la manera de dibujar el campo en las vistas
        widgets = {
            'skills': forms.CheckboxSelectMultiple()
        }

 