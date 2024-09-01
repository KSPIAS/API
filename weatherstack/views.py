from django.shortcuts import render
import requests
from weatherstack.models import apilogin ,api_request ,api_location ,api_current
from datetime import datetime, timezone, timedelta
from googletrans import Translator
import json
import os
import pandas as pd
# from pyspark.sql import SparkSession

# Create your views here.
def API_Weatherstack(request):
    city = "Chiang Mai"
    result = w_request(city)
    w_csv()
    r_csv()
    return render(request,"API_Weatherstack.html",{'get_api':result})

def wind_dir_to_th(wind_dir):
    if wind_dir == "N":
        return "ทิศเหนือ"
    elif wind_dir == "NE":
        return "ทิศตะวันออกเฉียงเหนือ"
    elif wind_dir == "E":
        return "ทิศตะวันออก"
    elif wind_dir == "SE":
        return "ทิศตะวันออกเฉียงใต้"
    elif wind_dir == "S":
        return "ทิศใต้"
    elif wind_dir == "SW":
        return "ทิศตะวันตกเฉียงใต้"
    elif wind_dir == "W":
        return "ทิศตะวันตก"
    elif wind_dir == "NW":
        return "ทิศตะวันตกเฉียงเหนือ"
    elif wind_dir == "SSW":
        return "ทิศใต้-ตะวันตกเฉียงใต้"
    elif wind_dir == "ESE":
        return "ทิศตะวันออกเฉียงใต้"
    else:
        return f"{wind_dir} ***ยังไม่ได้ระบุ"

def trans_to_th(text):
    translator = Translator()
    try:
        translated = translator.translate(text, src='en', dest='th')
        return translated.text
    except Exception as e:
        print(f"An error occurred: {e}")

########################### Read JSON ##########################
def read_file_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
################################################################

######################### Read/Write CSV #######################
def w_csv():
    all_fields = [field.name for field in api_location._meta.get_fields()]
    # print("all_fields" ,all_fields)
    data_location = api_location.objects.all()
    data_list = list(data_location.values(*all_fields))
    # print("Data List:", data_list)
    df = pd.DataFrame(data_list)
    # print(df)
    directory = "weatherstack/csv"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, "api_location.csv")
    try:
        df.to_csv(file_path ,index=False)
        print(f"DataFrame successfully saved to '{file_path}'.")
    except PermissionError:
        print(f"Permission denied. The file '{file_path}' may be open or in use.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    # return df
def r_csv():
    try:
        directory = "weatherstack/csv"
        file_path = os.path.join(directory, "api_location.csv")
        df = pd.read_csv(file_path ,dtype=str)
        print(df)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
################################################################

def w_request(city):
    try:
        current_date = datetime.now().date()
        current_month = datetime.now().month
        current_year = datetime.now().year
        total_in_month = api_request.objects.filter(data_date__month=current_month).filter(data_date__year=current_year).count()
        print(f"total_call_in_month: {total_in_month}")
        # get_api_request = api_request.objects.filter(query="Bangkok, Thailand").filter(data_date__date=current_datetime)
        
        ##get_api_request
        get_api_request = api_request.objects.filter(city__icontains=city).filter(data_date__date=current_date)
        for i in get_api_request:
            request_id = i.request_id
            type = i.type
            location = i.city
            language = i.language
            unit = i.unit
            data_date = i.data_date
        # offset = timezone(timedelta(hours=7))
        # data_date = data_date.date()
        # print(data_date)

        ##get_api_location
        get_api_location = api_location.objects.filter(request_id=request_id)
        for loc in get_api_location:
            location_id = loc.location_id
            name = loc.name
            country = loc.country
            region = loc.region
            timezone_id = loc.timezone_id
            local_time = loc.local_time
            f_utc_offset = float(loc.utc_offset)
            i_utc_offset = int(f_utc_offset)
            utc_offset = timedelta(hours=i_utc_offset)
            utc_local_time = local_time + utc_offset
        # print(f"utc_offset: {utc_offset}")

        ##get_api_current
        get_api_current = api_current.objects.filter(request_id=request_id)
        for cur in get_api_current:
            current_id = cur.current_id
            wind_speed = cur.wind_speed
            wind_degree = cur.wind_degree
            wind_dir = cur.wind_dir
            wind_dir_th = wind_dir_to_th(wind_dir)
            temperature = cur.temperature
            weather_descriptions = cur.weather_descriptions.replace("['","").replace("']","")
            weather_desc_trans = trans_to_th(weather_descriptions)

        # result = location + "-" + str(data_date)
        result_location = f"{name} ,{region} ,{country} ,{timezone_id} ,{utc_local_time}"
        result_win = f"ความเร็วลม : {wind_speed} กิโลเมตร/ชั่วโมง ,ทิศทางลม : {wind_dir_th}({wind_dir})"
        result_temp = f"อุณหภูมิ : {temperature} ℃"
        result_weather_desc = f"สภาพอากาศ : {weather_desc_trans}"
        result = f"{result_location} {result_win} {result_temp} {result_weather_desc}"

        data_date_file = data_date.date().strftime('%Y%m%d')
        file_path = f"weatherstack\json\weatherstack_{city}_{data_date_file}.json"
        data = read_file_json(file_path)
        print(file_path)
        # print(data)

        return result
    except:
        data_date = datetime.now()
        data_date_id = data_date.date()
        data_date_file = data_date.date().strftime('%Y%m%d')
        data_date = data_date.isoformat()
        get_apilogin = apilogin.objects.filter(name="weatherstack_current")
        city = city
        for i in get_apilogin:
            url = i.url
            pwd = i.pwd
        get_api = url+pwd+"&query="+city
        get_api = get_api.strip()
        if total_in_month < 245:
            response = requests.get(get_api).json()

            try:
                # Save JSON data to a file
                # Ensure directory exists
                file_path = f"weatherstack\json\weatherstack_{city}_{data_date_file}.json"
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                with open(file_path, 'w') as file:
                    json.dump(response, file, indent=4)
                print(f"Data successfully saved to {file_path}")
            except IOError as e:
                print(f"Failed to write to file: {e}")

            ##request
            try:
                js_request = response['request']
                # print(js_request)
                js_request_new = js_request.pop('query')
                js_request['city'] = js_request_new
                print(js_request)
                request_id=city+":"+str(data_date_id)
                api_request.objects.create(request_id=request_id,**js_request ,data_date=data_date)
                request_result = "Insert api_request success"
            except Exception as e:
                # Handle other potential errors (e.g., database errors)
                print(f"An unexpected error occurred: {e}")
                request_result = f"{e}"

            ##location
            try:
                js_location = response['location']
                # print(js_location)
                js_location_new = js_location.pop('localtime')
                js_location['local_time'] = js_location_new
                print(js_location)
                location_id=js_location['name']+" ,"+js_location['country']+":"+str(data_date_id)
                api_location.objects.create(location_id=location_id,request_id=request_id,**js_location,data_date=data_date)
                location_result = "Insert api_location success"
            except Exception as e:
                # Handle other potential errors (e.g., database errors)
                print(f"An unexpected error occurred: {e}")
                location_result = f"{e}"

            ##current
            try:
                js_current = response['current']
                print(js_current)
                current_id = location_id
                api_current.objects.create(current_id=current_id,request_id=request_id,**js_current ,data_date=data_date)
                current_result = "Insert api_current success"
            except Exception as e:
                # Handle other potential errors (e.g., database errors)
                print(f"An unexpected error occurred: {e}")
                current_result = f"{e}"

            result = f"{request_result} ,{location_result} ,{current_result}"
        else:
            result = "Usage limit has been reached"
        # print(response)
        # js_request = response['request']
        # api_request.objects.create(**js_request ,data_date=data_date)
        # api_request.objects.create(type='City',query='Bangkok, Thailand',language='en',unit='m',data_date=data_date)
        # result = "Insert request success"
        return result