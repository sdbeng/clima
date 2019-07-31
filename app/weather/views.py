import requests
from django.shortcuts import render
from django.conf import settings
from .models import City
from .forms import CityForm


def index(request):
    API_KEY = settings.API_KEY
    # print(f"LOG KEY {API_KEY}")
    URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    # URL = 'http://api.openweathermap.org/data/2.5/weather?id=2172797&appid={}'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        # print(request.POST)
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            # prevent duplicates
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                json_response = requests.get(URL.format(new_city, API_KEY)).json()
                
                if json_response['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist in the world!'
            else:
                err_msg = 'City already exists in database!'
        if err_msg:
            # don't forget to add these props to the context
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully'
            message_class = 'is-success'

    print(err_msg)
    form = CityForm()
    
    # print(res.text)
    # json_response = res.json()

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
    context = {
        'city_data': dest_cities,
        'form': form,
        'message': message,
        'message_class': message_class
        }

    # return render(request, 'weather/weather.html')
    return render(request, 'weather/weather.html', context)
