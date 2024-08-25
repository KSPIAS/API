from django.shortcuts import render
import requests
from weatherstack.models import apilogin ,api_request
from datetime import datetime, timezone, timedelta


# Create your views here.
def API_Weatherstack(request):
    query = "Thailand"
    result = w_request(query)
    return render(request,"API_Weatherstack.html",{'get_api':result})

def w_request(query):
    try:
        current_datetime = datetime.now().date()
        current_month = datetime.now().month
        current_year = datetime.now().year
        total_in_month = api_request.objects.filter(data_date__month=current_month).filter(data_date__year=current_year).count()
        print(f"total_call_in_month: {total_in_month}")
        # get_api_request = api_request.objects.filter(query="Bangkok, Thailand").filter(data_date__date=current_datetime)
        get_api_request = api_request.objects.filter(query__icontains=query).filter(data_date__date=current_datetime)
        for i in get_api_request:
            type = i.type
            location = i.query
            language = i.language
            unit = i.unit
            data_date = i.data_date
        # offset = timezone(timedelta(hours=7))
        # data_date = data_date.date()
        # print(data_date)
        data_date = "2024-08-25"
        result = location + "-" + str(data_date)
        return result
    except:
        data_date = datetime.now()
        data_date = data_date.isoformat()
        get_apilogin = apilogin.objects.filter(name="weatherstack_current")
        city = "Bangkok"
        for i in get_apilogin:
            url = i.url
            pwd = i.pwd
        get_api = url+pwd+"&query="+city
        get_api = get_api.strip()
        if total_in_month < 245:
            response = requests.get(get_api).json()
            js_request = response['request']
            api_request.objects.create(**js_request ,data_date=data_date)
            result = "Insert request success"
        else:
            result = "Usage limit has been reached"
        # print(response)
        # js_request = response['request']
        # api_request.objects.create(**js_request ,data_date=data_date)
        # api_request.objects.create(type='City',query='Bangkok, Thailand',language='en',unit='m',data_date=data_date)
        # result = "Insert request success"
        return result