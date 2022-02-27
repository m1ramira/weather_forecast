import requests
from django.shortcuts import render


def data_for_chart(row_data):
    """
    Function extracts temperature values by dates
    :param row_data: dict with data from api-request
    :return: list of date, list of temperatures
    """
    date_labels = []
    temps = []

    for i in row_data['list']:
        date_labels.append(i['dt_txt'][:-3])
        temps.append(i['main']['temp'])

    return date_labels, temps


def index(request):
    """
    Function create html-page with data of city's weather
    :param request: city request from API openweathermap
    :return: render html-page
    """
    app_id = 'b5ff588e642b2bb30dff7e70cd37f32b'
    if request.method == 'POST':
        city_name = request.POST['city']

        row_data = requests.get(
            'http://api.openweathermap.org/data/2.5/forecast',
            params={'q': city_name, 'units': 'metric', 'appid': app_id}
        ).json()

        if int(row_data['cod']) == 200:
            data = {
                'city': row_data['city']['name'],
                'country': row_data['city']['country'],
                'icon': 'http://openweathermap.org/img/w/' + row_data['list'][0]['weather'][0]['icon'] + '.png',
                'description': row_data['list'][0]['weather'][0]['description'],
                'temperature': row_data['list'][0]['main']['temp'],
                'feels_like': row_data['list'][0]['main']['feels_like'],
                'temperature_min': row_data['list'][0]['main']['temp_min'],
                'temperature_max': row_data['list'][0]['main']['temp_max'],
                'humidity': row_data['list'][0]['main']['humidity'],
                'pressure': row_data['list'][0]['main']['pressure'],
                'windspeed': row_data['list'][0]['wind']['speed'],
                'labels': data_for_chart(row_data)[0],
                'temps': data_for_chart(row_data)[1],
            }
        else:
            data = {}
    else:
        data = {}

    return render(request, "city_weather/index.html", data)
