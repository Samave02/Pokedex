from django.shortcuts import render
import urllib.request
import json
from http import HTTPStatus
from urllib.error import HTTPError
import requests
# Create your views here.

def inicio(request):
    return render(request, "main/inicio.html") 

def index(request):

    try:
        if request.method == 'POST':
            pokemon = request.POST['pokemon'].lower()
            pokemon = pokemon.replace(' ','%20')
            # Request de la api
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
            res = requests.get(url).json()
            # ----------------- variables de la api----------------------------------
            id,nombre,altura,peso = res['id'],res['name'],str(res['height']/10)+' m',str(res['weight'])+" lbs"
            tipo  = []
            imagen = res['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
            for i in res['types']:
                tipo.append(i['type']['name'])
            for i in res['abilities']:
                if i['is_hidden'] == True:
                    habiliadadOculta = i['ability']['name']
                else:
                    habilidad = i['ability']['name']

            # -------------------base de datos---------------------------------------
            data = {'id':id,'nombre':nombre,'tipo':tipo,'altura':altura,'peso':peso,'habilidad':habilidad,'habiliadadOculta':habiliadadOculta,'imagen':imagen}
            print(data)
        else:
            data = {}

        return render(request, "main/index.html", data)
    except HTTPError as e:
        if e.code == 404:
            return render(request, "main/404.html")
        else:
            return render(request, "main/404.html") 

