key = "AIzaSyC8Yg8zsn2E2YXROgYGaKz-LxiBU9QC5Ac"
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key=" + key


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
    hotels_lst = DynamicArray()
    for i in range(len(results_hotels)):
        hotels = {
            'name': results_hotels[i]['name'],
            'rating': results_hotels[i]['rating'],
            'address': results_hotels[i]['formatted_address'],
            'lat': results_hotels[i]['geometry']['location']['lat'],
            'lng': results_hotels[i]['geometry']['location']['lng']
        }

        hotels_lst.append(hotels)
    hotels_lst = sorted(hotels_lst, key=lambda x: x[1])

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
