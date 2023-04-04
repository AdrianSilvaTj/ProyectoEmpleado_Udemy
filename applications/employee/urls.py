from django.contrib import admin
from django.urls import path, include

from . import views 

app_name = "employee"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list-all/', views.EmployeeListView.as_view(), name='list-all'),
    path('list-by-area/<shortname>', views.EmployeeListByAreaView.as_view(), name='by-area'),
    path('list-by-job/<job>', views.EmployeeListByJobView.as_view()),
    path('list-by-kword/', views.EmployeeListByKwordView.as_view()),
    path('skills/<int:id>', views.EmployeeSkillsView.as_view()),
    path('<int:id>', views.EmployeeDetailView.as_view(), name = 'details'),    
    path('add/', views.EmployeeCreateView.as_view(), name='add'),    
    path('success/', views.Success.as_view(),name='success'),    
    path('update/<int:pk>', views.EmployeeUpdateView.as_view(),name='update'),    
    path('delete/<int:pk>', views.EmployeeDeleteView.as_view(),name='delete'),    
    path('admin/', views.EmployeeAdminView.as_view(), name='admin'),
]
