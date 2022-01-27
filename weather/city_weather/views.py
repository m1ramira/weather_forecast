import requests
from django.shortcuts import render


def index(request):
    app_id = 'b5ff588e642b2bb30dff7e70cd37f32b'
    if request.method == 'POST':
        city_name = request.POST['city']

        row_data = requests.get(
            'http://api.openweathermap.org/data/2.5/weather',
            params={'q': city_name, 'units': 'metric', 'appid': app_id}
        ).json()
        if row_data['cod'] == 200:
            data = {
                'city': row_data['name'],
                'country': row_data['sys']['country'],
                'icon': 'http://openweathermap.org/img/w/' + row_data['weather'][0]['icon'] + '.png',
                'description': row_data['weather'][0]['description'],
                'temperature': row_data['main']['temp'],
                'feels_like': row_data['main']['feels_like'],
                'temperature_min': row_data['main']['temp_min'],
                'temperature_max': row_data['main']['temp_max'],
                'humidity': row_data['main']['humidity'],
                'pressure': row_data['main']['pressure'],
                'windspeed': row_data['wind']['speed']
            }
            print(data)
        else:
            data = {}
    else:
        data = {}

    return render(request, "city_weather/index.html", data)
