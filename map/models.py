from django.db import models


class City(models.Model):
    name = models.CharField(max_length=20)
    #
    # def __init__(self, hotel=None, address=None, rating=None, lat=None, lng=None):
    #     self.hotel = hotel
    #     self.address = address
    #     self.rating = rating
    #     self.lat = lat
    #     self.lng = lng

    def __str__(self):
        return self.name
