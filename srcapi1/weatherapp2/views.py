# weatherapp2/views.py
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
import json


def get_weather_data(city):
    city = city.replace(' ','+')
    url = f'https://www.google.com/search?q=weather+of+{city}'
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.9"
    session = requests.Session()
    session.headers['user-agent'] = USER_AGENT
    session.headers['accept-language'] = LANGUAGE
    response = session.get(url)
    soup = bs(response.text, 'html.parser')
    # Extract Data and Add to Dictionary
    results = {}
    results['region'] = soup.find('div', attrs={'id':'wob_loc'}).text
    results['daytime'] = soup.find('div', attrs={'id':'wob_dts'}).text
    results['weather'] = soup.find('span', attrs={'id':'wob_dc'}).text
    results['temp'] = soup.find('span', attrs={'id':'wob_tm'}).text
    # print(results)
    return results


def weather_api(city):
    api_key = '8c9ec1251ef6026d3eabd241c7a1fa00'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    results = {}
    results['lon'] = data['coord']['lon']
    results['lat'] = data['coord']['lat']
    results['name'] =data['name']
    results['temp'] =data['main']['temp']
    results['humidity'] =data['main']['humidity']
    return results




# Create your views here.


def home_view(request):
    if request.method == 'GET' and 'city' in request.GET:
        city = request.GET.get('city')
        results = get_weather_data(city)
        context = {'results':results}
    else:
        context = {}

    return render(request, 'weatherapp/home.html', context)




def api_view(request):
    if request.method == "POST" and 'city' in request.POST:
        city = request.POST.get('city')
        results = weather_api(city)
        context = {'results':results}
    else:
        context= {}
    return render(request, 'weatherapp/api.html', context )



