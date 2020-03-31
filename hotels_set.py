"""
Python program to get a set of
places according to your search
query using Google Places API
"""

# importing required modules
import json
import requests
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
    for i in range(len(results)):
        hotels_dict[results[i]['name']] = (results[i]['formatted_address'], results[i]['rating'])
    return hotels_dict


if __name__ == "__main__":
    CITY = input('In what city do you want to search hotels?: ')
    print(create_hotels_dict(CITY))
