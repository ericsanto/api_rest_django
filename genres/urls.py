
from django.urls import path, include
from django.http import JsonResponse
from .views import *

urlpatterns = [
    path('', genre_create_list_view, name='genre-create-list'),
    path('genres/<int:pk>/', genre_detail_view, name='genre-detail-view')
]
