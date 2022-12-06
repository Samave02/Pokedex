from django.urls import path
from . import views

urlpatterns = [
    path('pokedex', views.index, name='index'),
    path('', views.inicio, name='inicio'),
]
