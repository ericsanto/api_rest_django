
from .models import *
from rest_framework import generics
from genres.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data=({'message': 'Genero criado com Sucesso'}, serializer.data), status=status.HTTP_201_CREATED, headers=headers)


# lISTANDO OS GÊNEROS
'''@csrf_exempt
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
        )'''


'''@csrf_exempt
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
        )'''


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Gênero excluído com sucesso'}, status=status.HTTP_204_NO_CONTENT)
