from django.contrib import admin

from django.contrib import admin
from .models import City, CityWeatherInfo ,APILog

admin.site.register(City)
admin.site.register(CityWeatherInfo)

@admin.register(APILog)
class APILogAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'ip_address', 'endpoint', 'method', 'name_city')
    search_fields = ('user__username', 'ip_address', 'endpoint', 'name_city')
    list_filter = ('method', 'endpoint', 'timestamp')