from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def str(self):
        return self.name

class CityWeatherInfo(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    recorded_at = models.DateTimeField()

    def str(self):
        return f"{self.city.name} - {self.temperature}°C at {self.recorded_at}"



class APILog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    name_city = models.CharField(max_length=255, blank=True, null=True)

    def str(self):
        return f"{self.user} - {self.endpoint} - {self.method} - {self.timestamp}"