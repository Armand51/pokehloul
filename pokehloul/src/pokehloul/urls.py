"""pokehloul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Pokescrap.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-to-scrap/', add_to_scrap, name='add_to_scrap'),
    path('what-to-scrap/', what_to_scrap, name='what_to_scrap'),
    path('what-to-scrap/random', random_to_scrap, name='what_to_scrap_random'),
    path('add-to-data/P', add_to_dataP, name='add-to-data-P'),
    path('add-to-data/T', add_to_dataT, name='add-to-data-T'),
    path('add-to-data/A', add_to_dataA, name='add-to-data-A')
]
