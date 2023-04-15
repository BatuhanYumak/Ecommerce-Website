from django.contrib import admin
from django.urls import include, path
from django.urls import path
from django.urls import path

urlpatterns = [
    path('', include('webshop.urls')),
    path('admin/', admin.site.urls),  


]
