from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   return render(request, 'cs/home.html')

def about(request):
    return HttpResponse("<p> yeet </p>")

# Create your views here.
