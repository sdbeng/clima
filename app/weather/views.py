import requests
from django.shortcuts import render
from django.conf import settings
from .models import City
from .forms import CityForm


def index(request):
    # city = 'San Diego'
    API_KEY = settings.API_KEY
    # print(f"LOG KEY {API_KEY}")
    URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    # URL = 'http://api.openweathermap.org/data/2.5/weather?id=2172797&appid={}'

    if request.method == 'POST':
        print(request.POST)
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    # print(f"LOG URL - {URL}")
    # res = requests.get(URL.format(city))
    # res = requests.get(URL)
    # print(res.text)
    # json_response = res.json()
    # print(json_response)
    # iterate over the city_data to get temp from multiple cities
    # first, get all cities in database
    cities = City.objects.all()
    # create an empty list to hold all cities
    dest_cities = []

    try:
        for city in cities:       
            # city must be passed in order the requests call succeed
            json_response = requests.get(URL.format(city, API_KEY)).json()
            # print(json_response)
            # create a dict to retrieve the data
            city_data = {
                'city': city.name,
                'temperature': json_response['main']['temp'],
                'description': json_response['weather'][0]['description'],
                'icon': json_response['weather'][0]['icon'],
            }
            dest_cities.append(city_data)
    except KeyError:
        pass
    # except EXCEPTION as e:
    #     pass
    print(f"LOG dest_cities {dest_cities} ")

    # define context
    context = {'city_data': dest_cities, 'form': form}

    # return render(request, 'weather/weather.html')
    return render(request, 'weather/weather.html', context)
