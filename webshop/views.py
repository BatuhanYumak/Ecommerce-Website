from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from products.models import Product
from contactform.forms import ContactForm
from contactform.models import ContactModel
from django.core.mail import EmailMessage


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
            # Verwerk de formuliergegevens
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Sla de gegevens op in de database
            entry = ContactModel(name=name, email=email, message=message)
            entry.save()

            return redirect('succes')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def succes(request):
    succes_message = "Het formulier is succesvol verstuurd!"  # Succesbericht
    return render(request, 'succes.html', {'succes_message': succes_message})      

def succes(request):
    template = loader.get_template('succes.html')
    return HttpResponse(template.render())


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']


#         EmailMessage(
#                'Contact Form Submission from {}'.format(name),
#                message,
#                'justyumak@gmail.com', # Send from (your website)
#                ['justyumak@gmail.com'], # Send to (your admin email)
#                [],
#                reply_to=[email] # Email from the form to get back to
#            ).send()

#         return redirect('success')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})    
