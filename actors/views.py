from rest_framework import generics
from actors.models import *
from actors.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from authentication.permissions import IsAdminOrReadyOnly


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrReadyOnly,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data=({'message': 'Ator criado com sucesso!'}, serializer.data), status=status.HTTP_201_CREATED, headers=headers)


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'Ator deletado com sucesso!'})
