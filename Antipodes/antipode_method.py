from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform


class Geopoint:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def closet_parallel(self):
        return round(self.latitude)

    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat=self.latitude, lng=self.longitude)
        time_now = datetime.now(timezone(timezone_string))
        return time_now

    def get_weather(self):
        weather = Weather(apikey="26631f0f41b95fb9f5ac0df9a8f43c92", lat=self.latitude, lon=self.longitude)
        return weather.next_12h_simplified()

    @classmethod
    def ramdon(cls):
        return cls(uniform(90, -90), uniform(180, -180))


print(Geopoint.ramdon().closet_parallel())
# with the classmethod no need define latitud and longitude to the class

geo = Geopoint(31.4208, 64.4992)
print(geo.get_time())
print(geo.get_weather())
