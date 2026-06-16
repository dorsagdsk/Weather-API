from django.contrib.auth import authenticate
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import City, CityWeatherInfo,APILog
from .serializers import CitySerializer, CityWeatherInfoSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

class LoginAPIView(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        print(username)
        password = request.data.get('password')
        print(password)
        user = authenticate(username=username, password=password)

        if user is not None:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                return Response({'detail': 'Token not found. Please contact support.'},
                                status=status.HTTP_401_UNAUTHORIZED)

            response = JsonResponse({
                'token': token.key,

                'username': user.username
            })
            response.set_cookie(
                key='Token',
                value=token.key,
                httponly=True,
                samesite='Lax',
                max_age=86400
            )
            return response
        else:
            return Response({'detail': 'Invalid credentials'})


class CityListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        perform_logging(request, '/cities/api/', 'GET')
        return Response(serializer.data)

class WeatherInfoView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        city_name = request.data.get('name_city', '').strip()

        if not city_name:
            return Response({'error': 'name_city is required'}, status=status.HTTP_400_BAD_REQUEST)

        city = City.objects.filter(name__iexact=city_name).first()
        if not city:
            return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)

        latest_weather = CityWeatherInfo.objects.filter(city=city).order_by('-recorded_at').first()
        if not latest_weather:
            return Response({'error': 'No weather data available for this city'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CityWeatherInfoSerializer(latest_weather)
        perform_logging(request, '/weather/api/', 'POST',city_name)
        return Response(serializer.data)
def perform_logging(request, endpoint, method, name_city=None):
    APILog.objects.create(
        user=request.user if request.user.is_authenticated else None,
        timestamp=now(),
        ip_address=request.META.get('REMOTE_ADDR'),
        endpoint=endpoint,
        method=method,
        name_city=name_city
    )