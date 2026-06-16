from rest_framework import serializers
from main.models import City, CityWeatherInfo

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'latitude', 'longitude']

class CityWeatherInfoSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = CityWeatherInfo
        fields = ['id', 'city', 'temperature', 'recorded_at']