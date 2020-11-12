from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cs/', include('cs.urls')),
    path('admin/', admin.site.urls),
]
