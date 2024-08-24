from django.shortcuts import render
import requests
from weatherstack.models import apilogin ,api_request
import json

# Create your views here.
def API_Weatherstack(request):
    get_apilogin = apilogin.objects.filter(name="weatherstack_current")
    city = "Bangkok"
    for i in get_apilogin:
        url = i.url
        pwd = i.pwd
    get_api = url+pwd+"&query="+city
    get_api = get_api.strip() 
    response = requests.get(get_api).json()
    print(response)
    return render(request,"API_Weatherstack.html",{'get_apilogin':response})

#####For test insert
# def API_Weatherstack(request):
#     json_txt = {'request': {'type': 'City', 'query': 'Bangkok, Thailand', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Bangkok', 'country': 'Thailand', 'region': 'Krung Thep', 'lat': '13.750', 'lon': '100.517', 'timezone_id': 'Asia/Bangkok', 'localtime': '2024-08-18 19:47', 'localtime_epoch': 1724010420, 'utc_offset': '7.0'}, 'current': {'observation_time': '12:47 PM', 'temperature': 31, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Partly cloudy'], 'wind_speed': 20, 'wind_degree': 190, 'wind_dir': 'S', 'pressure': 1007, 'precip': 0, 'humidity': 75, 'cloudcover': 25, 'feelslike': 37, 'uv_index': 1, 'visibility': 10, 'is_day': 'no'}}
#     request = json_txt['request']
#     req_list = []
#     req_data = []
#     api_req = []
#     for req in request:
#         req_list.append(req)
#         req_data.append(request[req])
#         api_req.append(f"{req}='{request[req]}'")
#     api_req = ",".join(api_req)
#     # api_request = api_request(api_req)
#     api_request = api_request(type='City',query='Bangkok, Thailand',language='en',unit='m')
#     api_request.save()
#     return render(request,"API_Weatherstack.html",{'get_apilogin':request})