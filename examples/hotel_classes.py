import wikipedia


class Hotels:
    def __init__(self, name, address, rating):
        self.name = name
        self.address = address
        self.rating = rating
        self.get_description = None

    def __repr__(self):
        return "{}: ({}, {})".format(self.name, self.address, self.rating)

    def __str__(self):
        return "{}: ({}, {})".format(self.name, self.address, self.rating)


    def description(self, city):
        find = self.name + city
        self.get_description = wikipedia.summary(find)
        return self.get_description

hotel = Hotels("Grand Hotel in Lviv", "13 Svobody Ave, Lviv, Lviv Oblast, Ukraine, 79000", 4.5)
# Hotels.name = "Grand Hotel in Lviv 13"
# Hotels.address = "Svobody Ave, Lviv, Lviv Oblast, Ukraine, 79000"
# Hotels.rating = 4.5
# print(Hotels.name, Hotels.address, Hotels.rating)
print(hotel.description)
print(hotel)