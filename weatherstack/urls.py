from django.urls import path
from weatherstack import views

urlpatterns = [
    path('',views.API_Weatherstack),
]