from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cegep/', views.cegep, name='cs-cegep'),
    path('combiningstudies/', views.combining_studies, name='cs-combiningstudies'),
    path('freshman/', views.freshman, name='cs-freshman'),
    path('generalinfo', views.general_info, name='cs-generalinfo'),
    path('internships', views.internships, name='cs-internships'),
    path('major', views.major, name='cs-major'),
    path('transfers', views.transfers, name='cs-transfers'),
    path('undergrad', views.undergrad, name='cs-undergrad'),
    path('whycs', views.whycs, name='cs-whycs'),
    path('areas', views.areas, name='cs-areas'),
    path('Undergraduate', views.undergraduate, name='cs-undergraduate'),
    path('faculty', views.faculty, name='cs-faculty'),
]
