import pandas as pd
import json
# from weatherstack.models import api_request

json_txt = {'request': {'type': 'City', 'query': 'Bangkok, Thailand', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Bangkok', 'country': 'Thailand', 'region': 'Krung Thep', 'lat': '13.750', 'lon': '100.517', 'timezone_id': 'Asia/Bangkok', 'localtime': '2024-08-18 19:47', 'localtime_epoch': 1724010420, 'utc_offset': '7.0'}, 'current': {'observation_time': '12:47 PM', 'temperature': 31, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Partly cloudy'], 'wind_speed': 20, 'wind_degree': 190, 'wind_dir': 'S', 'pressure': 1007, 'precip': 0, 'humidity': 75, 'cloudcover': 25, 'feelslike': 37, 'uv_index': 1, 'visibility': 10, 'is_day': 'no'}}
# print("request = " , json_txt['request'])
# print("location = " , json_txt['location'])
# print("current = " , json_txt['current'])

#request
# type = json_txt['request']['type']
# query = json_txt['request']['query']
# language = json_txt['request']['language']
# unit = json_txt['request']['unit']
# print(type ,query ,language ,unit)
request = json_txt['request']
# print(request)
req_list = []
req_data = []
api_req = []
for req in request:
    req_list.append(req)
    req_data.append(request[req])
    api_req.append(f"{req}='{request[req]}'")
# print(req_list)
# print(req_data)
# req_data = "','".join(req_data)
# req_data = f"'{req_data}'"
api_req = ",".join(api_req)
print(req_data)
print(api_req)
# Create a new Person object
# api_request = api_request(name='Alice', age=30, email='alice@example.com')
# api_request = api_request(api_req)

# Save the object to the database
# api_request.save()


#location
name = json_txt['location']['name']
country = json_txt['location']['country']
region = json_txt['location']['region']
lat = json_txt['location']['lat']
lon = json_txt['location']['lon']
timezone_id = json_txt['location']['timezone_id']
localtime = json_txt['location']['localtime']
localtime_epoch = json_txt['location']['localtime_epoch']
utc_offset = json_txt['location']['utc_offset']
timezone_id = json_txt['location']['timezone_id']
# print(name ,country ,region ,lat ,lon ,timezone_id ,localtime ,localtime_epoch ,utc_offset ,timezone_id)

#current
# observation_time = json_txt['current']['observation_time']
# temperature = json_txt['current']['temperature']
# weather_code = json_txt['current']['weather_code']
# weather_icons = json_txt['current']['weather_icons']
# weather_descriptions = json_txt['current']['weather_descriptions']
# wind_speed = json_txt['current']['wind_speed']
# wind_degree = json_txt['current']['wind_degree']
# wind_dir = json_txt['current']['wind_dir']
# pressure = json_txt['current']['pressure']
# precip = json_txt['current']['precip']
# humidity = json_txt['current']['humidity']
# cloudcover = json_txt['current']['cloudcover']
# feelslike = json_txt['current']['feelslike']
# uv_index = json_txt['current']['uv_index']
# visibility = json_txt['current']['visibility']
# is_day = json_txt['current']['is_day']