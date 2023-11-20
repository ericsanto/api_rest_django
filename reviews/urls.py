from django.urls import path
from reviews.views import *


urlpatterns = [
    path('reviews', ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(),
         name='reviews-retrieve-update-destroy')
]
