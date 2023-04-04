from django.contrib import admin
from .models import Employee, Skill

admin.site.register(Skill)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'job',
        'departament',
        'full_name', #Llama a la funcion del mismo nombre
        )
    search_fields = ('first_name','last_name',)
    list_filter = ('job','departament','skills',)
    filter_horizontal = ('skills',)
    
    def full_name(self, obj):
        return obj.first_name + ' '+ obj.last_name

admin.site.register(Employee, EmployeeAdmin)