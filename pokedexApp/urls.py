from django.urls import path
from .import views

# Pagina de inicio
urlpatter = [
    path('', views.index, name = 'index'),
]