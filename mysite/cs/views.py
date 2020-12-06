from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'cs/homepage.html', context)

def cepep(request):
    return render(request, 'cs/cegep.html')

def about(request):
    return HttpResponse("<p> test </p>")

# Create your views here.
