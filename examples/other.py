"""
Python program to get a set of
places according to your search
query using Google Places API
"""

# importing required modules
import json
import requests
import wikipedia
from key import key


def create_hotels_dict(city):
    """
    (string) -> (dict)
    Function returns dictionary with hotels name as a key
    and a tuple of it's location and rating as a value.
    """
    api_key = key

    # url variable store url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # The text string on which to search
    # get method of requests module
    # return response object
    query = "Hotels in" + city
    hotels_request = requests.get(url + 'query=' + query +
                                  '&key=' + api_key)

    # json method of response object convert
    #  json format data into python format data
    whole_json = hotels_request.json()
    # now whole_json contains list of nested dictionaries
    # write whole_json in JSON file
    with open('data.json', 'w', encoding='utf-8') as fle:
        json.dump(whole_json, fle, ensure_ascii=False, indent=4)
    results = whole_json['results']

    hotels_dict = {}
    hotels_dict['city hotels'] = []
    for i in range(len(results)):
        find = results[i]['name'] + city
        try:
            description = wikipedia.summary(find)
        except wikipedia.exceptions.PageError:
            description = ""


        hotels_dict['city hotels'].append({
            'name': results[i]['name'],
            'address': results[i]['formatted_address'],
            'rating': results[i]['rating'],
            "lat": results[i]["geometry"]['location']['lat'],
            "lng": results[i]["geometry"]['location']['lng'],
            'description' : description
        })

    with open("city_hotels.json", 'w', encoding='utf-8') as fle:
        json.dump(hotels_dict, fle, ensure_ascii=False, indent=4)

        # hotels_dict[results[i]['name']] = (results[i]['formatted_address'], results[i]['rating'])
    # return hotels_dict

    # hotels_list = []
    # for i in range(len(results)):
    #     hotel = Hotels(results[i]['name'], results[i]['formatted_address'], results[i]['rating'])
    #
    #     try:
    #         hotels_list.append([hotel, hotel.description(city)])
    #     except wikipedia.exceptions.PageError:
    #         hotels_list.append("0")
    #
    # return hotels_list






if __name__ == "__main__":
    # CITY = input('In what city do you want to search hotels?: ')
    CITY = "Lviv"
    create_hotels_dict(CITY)
