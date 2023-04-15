from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect


def index (request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

