
from django.urls import path, include
from django.http import JsonResponse
from .views import *

urlpatterns = [
    path('genres', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(),
         name='genre-detail-view')
]
