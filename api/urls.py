from django.urls import path
from .views import CityListView, WeatherInfoView , LoginAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('cities/api/', CityListView.as_view(), name='city-list'),
    # path('weather/api/', WeatherInfoView.as_view(), name='weather-info'),
    # path('api/token/', obtain_auth_token, name='api-token'),
    # path('api/login', LoginAPIView.as_view(), name='login'),


    path('cities/', CityListView.as_view(), name='city-list'),
    path('weather/', WeatherInfoView.as_view(), name='weather-info'),
    path('token/', obtain_auth_token, name='api-token'),
    path('login/', LoginAPIView.as_view(), name='login'),
]