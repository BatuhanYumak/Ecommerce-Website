from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from products.models import Product
from contactform.models import ContactForm
from contactform.forms import ContactForm as ContactFormForm
from django.core.mail import EmailMessage
from django.conf import settings

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

def succes(request):
    template = loader.get_template('succes.html')
    return HttpResponse(template.render())

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
   return HttpResponse('Success!')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            EmailMessage(
               'Contact Form Submission from {}'.format(name),
               message,
               'form-response@example.com', # Send from (your website)
               ['JohnDoe@gmail.com'], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to
           ).send()

            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})