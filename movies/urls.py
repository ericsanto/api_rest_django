from django.urls import path
from movies.views import *

urlpatterns = [
    path('movies', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(),
         name='movies-retrieve-update-destroy')
]
