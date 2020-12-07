from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'cs/homepage.html', context)

def cegep(request):
    return render(request, 'cs/cegep.html')

def combining_studies(request):
    return render(request, 'cs/combining_studies.html')

def freshman(request):
    return render(request, 'cs/freshman.html')

def general_info(request):
    return render(request, 'cs/general_info.html')

def internships(request):
    return render(request, 'cs/internships.html')

def major(request):
    return render(request, 'cs/major.html')

def transfers(request):
    return render(request, 'cs/transfers.html')

def undergrad(request):
    return render(request, 'cs/undergrad.html')

def whycs(request):
    return render(request, 'cs/whycs.html')

def areas(request):
    return render(request, 'cs/Areas.html')

def faculty(request):
    return render(request, 'cs/Faculty.html')

def undergraduate(request):
    return render(request, 'cs/Undergraduate.html')