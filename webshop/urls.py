from django.urls import path
from . import views
from django.http import HttpResponse
from django.shortcuts import render


# Hier maak path's aan. Dit gebruik ik voor om de gebruiker naar een andere pagina te sturen.

urlpatterns = [
    # Dit is de homepage
    path('', views.index, name='index'),
    path('console', views.console, name='console'),

    

]
