from django.urls import path
from rest_framework_simplejwt.views import *

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(),
         name='authentication_obtain_token'),



]
