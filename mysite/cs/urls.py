from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='cs-about'),
    path('cegep/', views.cegep, name='cs-cegep'),
]
