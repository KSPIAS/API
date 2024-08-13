from django.shortcuts import render
import requests

# Create your views here.
def API_COVID(request):
    response = requests.get('https://covid-api.com/api/regions').json()
    # response = json.loads(response)
    return render(request,"API_COVID.html",{'response':response})