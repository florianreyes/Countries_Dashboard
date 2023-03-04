import requests 
import json

def get_all_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    countries = [country['name']['common'].lower() for country in response.json()]
    return countries

def get_country_info(name):
    url = "https://restcountries.com/v3.1/name/{}".format(name)
    response = requests.get(url)
    return response.json()

country = "argentina"
print(get_country_info(country)[0]['latlng'][0])