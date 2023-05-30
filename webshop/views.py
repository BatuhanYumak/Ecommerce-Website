from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from products.models import Product
from contactform.forms import ContactForm

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


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('succes')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def succes(request):
    template = loader.get_template('succes.html')
    return HttpResponse(template.render())

