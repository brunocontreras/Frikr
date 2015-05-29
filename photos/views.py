from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    html = '<strong>Hola mundo!</strong>'
    return HttpResponse(html)