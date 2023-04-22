from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Product
        

def console(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'console.html', context)