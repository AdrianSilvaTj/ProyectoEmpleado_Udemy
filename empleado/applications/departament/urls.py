from django.contrib import admin
from django.urls import path
from . import views

app_name = "departament"
urlpatterns = [
    path('list-all/', views.DepartamentListView.as_view(), name='list-all'),
    path('<int:pk>', views.DepartamentDetailView.as_view(), name='details'),
       
]