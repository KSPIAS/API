from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def API_Weatherstack(request):
    return render(request,"API_Weatherstack.html")