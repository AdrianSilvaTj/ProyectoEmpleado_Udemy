from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "employee"
urlpatterns = [
    path('list-all/', views.EmployeeListView.as_view(), name='list-all'),
    path('list-by-area/<shortname>', views.EmployeeListByAreaView.as_view()),
    path('list-by-job/<job>', views.EmployeeListByJobView.as_view()),
    path('list-by-kword/', views.EmployeeListByKwordView.as_view()),
    path('skills/<int:id>', views.EmployeeSkillsView.as_view()),
    path('<int:id>', views.EmployeeDetailView.as_view()),    
    path('add/', views.EmployeeCreateView.as_view()),    
    path('success/', views.Success.as_view(),name='success'),    
]
