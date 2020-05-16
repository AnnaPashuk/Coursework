import requests
import sys
import wikipedia
from django.shortcuts import render
from .models import City
from .forms import CityForm
from .templates.dinamic_array import DynamicArray


# # Create your views here.
# def index(request):
#     key = "AIzaSyC8Yg8zsn2E2YXROgYGaKz-LxiBU9QC5Ac"
#     url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key=" + key
#
#     city = request
#     query = "Hotels in " + city
#     res_city = requests.get(url.format(query)).json()
#     results = res_city['results']
#
#     if request.method == 'POST':
#         form = CityForm(request.POST)
#         form.save()
#
#     form = CityForm()
#
#     for i in range(len(results)):
#
#         hotels_dict = {'hotel': results[i]['name'],
#                         'address': results[i]['formatted_address'],
#                         'rating': results[i]['rating'],
#                         'lat':  results[i]['geometry']['location']['lat'],
#                         'lng': results[i]['geometry']['location']['lng']}
#     context = {'hotels_info': hotels_dict, 'form': form}
#     print(context)
#     return render(request, 'hotels/index.html', context)


def info(request):
    key = "AIzaSyC8Yg8zsn2E2YXROgYGaKz-LxiBU9QC5Ac"
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key=" + key


    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    all_cities = DynamicArray()

    for city in cities:
        # request for info about city
        query = city
        res_city = requests.get(url.format(query)).json()
        results = res_city['results'][0]

        # request info about hotels
        query_hotel = "Hotels in " + city.name
        res_hot = requests.get(url.format(query_hotel)).json()
        results_hotels = res_hot['results']
        hotels_lst = []
        for i in range(len(results_hotels)):
            hotels = {
                'name': results_hotels[i]['name'],
                'rating': results_hotels[i]['rating'],
                'lat': results_hotels[i]['geometry']['location']['lat'],
                'lng': results_hotels[i]['geometry']['location']['lng']
            }
            hotels_lst.append(hotels)

        city_info = {
            'city': city.name,
            'description_p1': str(wikipedia.summary(city))[:150],
            'description_p2': str(wikipedia.summary(city))[150:],
            'lat': results['geometry']['location']['lat'],
            'lng': results['geometry']['location']['lng'],
            'hotels': hotels_lst
        }
        all_cities.append(city_info)
            # names.append(city.name)
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'hotels/index.html', context)



