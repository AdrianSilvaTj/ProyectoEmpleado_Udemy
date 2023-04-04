from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('home/', views.IndexView.as_view()),
    path('list/', views.PruebaListView.as_view()),
    path('listModel/', views.ModelPruebaListView.as_view()),
]