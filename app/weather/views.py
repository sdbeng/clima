import requests
from django.shortcuts import render

# Create your views here.
URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=963e410024d4bea5f9a528a77cd58039'


def index(request):
    city = 'Las Vegas'
    res = requests.get(URL.format(city))
    # print(res.text)
    json_response = res.json()
    print(json_response)

    # create a dict to retrieve the data
    city_data = {
        'city': city,
        # 'temperature': json_response['main']['temp'],
        'description': json_response['weather'][0]['description'],
        'icon': json_response['weather'][0]['icon'],
    }

    print(city_data)
    # define context
    context = {'city_data': city_data}

    # return render(request, 'weather/weather.html')
    return render(request, 'weather/weather.html', context)
