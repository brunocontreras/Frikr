from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo

# Create your views here.

def home(request):
    photos = Photo.objects.all().order_by('-created_on')
    context = {
        'photo_list': photos[:5],
    }
    return render(request, 'photos/home.html', context)