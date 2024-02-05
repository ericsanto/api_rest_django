from django.urls import path
from rest_framework_simplejwt.views import *

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(),
         name='authentication_obtain_token'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(),
         name='authentication_token_refresh'),
    path('authentication/token/verify/', TokenVerifyView.as_view(),
         name='authentication_verify_view'),



]
