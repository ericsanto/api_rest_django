from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


# lISTANDO OS GÊNEROS
@csrf_exempt
def genre_create_list_view(request):
    # JEITO MANUAL
    if str(request.method) == 'GET':
        genres = Genre.objects.all()
        data = []
        for genre in genres:
            data.append({'id': genre.id, 'name': genre.name})
        return JsonResponse(data, safe=False)
    elif str(request.method) == 'POST':
        # o arquivo json tera seu body decodificado em formato 'utf-8'
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name},
            status=201,  # esse parâmetro status confirma a criação
        )


@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if str(request.method) == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    elif str(request.method) == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            {'id': genre.id, 'name': genre.name},
            status=200,
        )
    elif str(request.method) == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'message': 'Gênero excluído com sucesso!'},
            status=204,
        )
