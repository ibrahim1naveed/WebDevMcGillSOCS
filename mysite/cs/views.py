from django.shortcuts import render
from django.http import HttpResponse

news = [
    {
        'author' : 'McGill Robotics',
        'title' : 'Robotics news',
        'content' : 'First post content',
        'date_posted' : 'Posted today'
    },
    {
        'author' : 'Compete McGill',
        'title' : 'Competitive programming news',
        'content' : 'Second post content',
        'date_posted' : 'Posted today'
    }
]


def index(request):
    context = {
        'posts' : news
    }
    return render(request, 'cs/home.html', context)

def about(request):
    return HttpResponse("<p> yeet </p>")

# Create your views here.
