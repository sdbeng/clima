import requests
from django.shortcuts import render

# Create your views here.
api = '963e410024d4bea5f9a528a77cd58039'


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={api}'

    city = 'Las Vegas'
    res = requests.get(url.format(city))
    print(res.text)
    json_response = res.json()

    # create a dict to retrieve the data
    city_data = {
        'city': city,
        'temperature': json_response['main']['temp'],
        'description': json_response['weather'][0]['description'],
        'icon': json_response['weather'][0]['icon'],
    }

    print(city_data)

    return render(request, 'weather/weather.html')
