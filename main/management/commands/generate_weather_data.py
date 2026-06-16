import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from main.models import City, CityWeatherInfo

class Command(BaseCommand):
    help = "Generate random weather data for all cities"

    def handle(self, *args, **kwargs):
        cities = City.objects.all()
        if not cities:
            self.stdout.write(self.style.WARNING("No cities found! Please add cities first."))
            return

        for city in cities:
            for days_ago in [365, 10, 3, 1, 0]:  # سال گذشته، 10 روز قبل، 3 روز قبل، دیروز، امروز
                random_temp = round(random.uniform(-10, 40), 2)
                recorded_at = datetime.now() - timedelta(days=days_ago)
                CityWeatherInfo.objects.create(city=city, temperature=random_temp, recorded_at=recorded_at)

        self.stdout.write(self.style.SUCCESS("Weather data generated successfully!"))