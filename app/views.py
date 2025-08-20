from django.shortcuts import render
import requests

# Create your views here.
def index(request):

    city = request.GET.get('city', 'bangalore')

    api_key = 'fc15e61175282b292157438550723606'

    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    print(api_url)

    api =  requests.get(api_url).json()

    temperature = api['main']['temp']

    city = api['name']

    country = api['sys']['country']

    wind_speed = api['wind']['speed']

    humidity = api['main']['humidity']

    icon_id = api['weather'][0]['icon']
    weather = api['weather'][0]['main']
    description = api['weather'][0]['description']

    icon_url = f'https://openweathermap.org/img/wn/{icon_id}@2x.png'
    print(icon_url)

    return render(request, 'index.html', {'temperature':temperature, 'city':city, 'country': country, 'wind_speed': wind_speed, 'humidity': humidity, 'weather':weather, 'description':description, 'icon_url': icon_url})




    
   


    