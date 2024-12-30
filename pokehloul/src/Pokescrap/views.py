from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Pokedata.models import *
from Pokescrap.models import To_Scrap
from django.shortcuts import render
from Pokescrap.scripts.one_link import scrap_attaque, scrap_talent, scrap_pokemon


def what_to_scrap(request):
    if request.method == 'GET':
        scraping_list = To_Scrap.objects.all()
        return render(request, 'Pokescrap/what_to_scrap.html', context={"scraping_list": scraping_list})
    if request.method == 'POST':
        type_element = request.POST.get('type_element')
        if type_element == 'T':
            scrap_talent(request.POST.get('url'))
        elif type_element == 'A':
            scrap_attaque(request.POST.get('url'))
        elif type_element == 'P':
            scrap_pokemon(request.POST.get('url'))
        return HttpResponse("<html><body><h1>C'est scrapé !</h1></body></html>")
    
def random_to_scrap(request):
    if request.method == 'GET':
        return render(request, 'Pokescrap/random_to_scrap.html')
    if request.method == 'POST':
        number_to_scrap = int(request.POST.get('n'))
        type_element = request.POST.get('categ')
        print(number_to_scrap)
        scraping_list = To_Scrap.objects.filter(type_element=type_element, is_scraped=False).order_by('?')[:number_to_scrap]
        print(len(scraping_list))
        for i in scraping_list:
            if type_element == 'T':
                scrap_talent(i.url)
            elif type_element == 'A':
                scrap_attaque(i.url)
            elif type_element == 'P':
                scrap_pokemon(i.url)
        return HttpResponse("<html><body><h1>C'est scrapé !</h1></body></html>")

    


@csrf_exempt
def add_to_scrap(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        type_element = data.get('type_element')
        url = data.get('url')

        if not all([name, type_element, url]):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        To_Scrap.objects.create(name=name, type_element=type_element, url=url)
        return JsonResponse({'message': 'To_Scrap created successfully'}, status=201)

    return JsonResponse({'error': 'Invalid method'}, status=405)




@csrf_exempt
def add_to_dataP(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data['name']
        picture_url = data['picture_url']
        url = data['url']
        if not all([name, picture_url, url]):
            return JsonResponse({'error': 'All fields are required'}, status=400)
        Pokemon.objects.create(name=name, picture_url=picture_url, url=url)
        return JsonResponse({'message': 'To_Scrap created successfully'}, status=201)

    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def add_to_dataT(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data['name']
        url = data['url']
        description = data['description']
        effet_combat = data['effet_combat']
        effet_terrain = data['effet_terrain']
        if not all([name, url]):
            return JsonResponse({'error': 'All fields are required'}, status=400)
        Talent.objects.create(name=name, url=url, description=description, effet_combat=effet_combat, 
                              effet_terrain=effet_terrain)
        return JsonResponse({'message': 'To_Scrap created successfully'}, status=201)

    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def add_to_dataA(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data['name']
        url = data['url']
        if not all([name, url]):
            return JsonResponse({'error': 'All fields are required'}, status=400)
        Attaque.objects.create(name=name, url=url)
        return JsonResponse({'message': 'To_Scrap created successfully'}, status=201)

    return JsonResponse({'error': 'Invalid method'}, status=405)
