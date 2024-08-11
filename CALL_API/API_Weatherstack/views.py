from django.shortcuts import render
import requests
# import json

# Create your views here.
def index(request):
    return render(request,"index.html")

def API_Weatherstack(request):
    return render(request,"API_Weatherstack.html")

def API_COVID(request):
    response = requests.get('https://covid-api.com/api/regions').json()
    # response = json.loads(response)
    return render(request,"API_COVID.html",{'response':response})