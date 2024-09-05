from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='haribhakt.index'),      
    path("create/", views.create, name='haribhakt.create'), 
    path("update/<id>/", views.update, name='haribhakt.update'),      
    path("edit/<id>/", views.edit, name='haribhakt.edit')    
    
]
