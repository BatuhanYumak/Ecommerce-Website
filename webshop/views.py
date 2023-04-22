from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from products.models import Product

def index (request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def console(request):
    template = loader.get_template('console.html')
    return HttpResponse(template.render())
    
def console(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'console.html', context)