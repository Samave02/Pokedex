from django.shortcuts import render
import requests
import pandas as pd
# Create your views here.
def index (request):
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
                hab_oculta = i['ability']['name']
            else:
                habilidad = i['ability']['name']

        # -------------------base de datos---------------------------------------
        data = {'id':id,'nombre':nombre,'tipo':tipo,'altura':altura,'peso':peso,'habilidad':habilidad,'habiliadadOculta':hab_oculta,'imagen':imagen}
        print(data)
    else:
        data = {}
    return render(request,'main/pokedex.html',data)