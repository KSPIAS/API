from django.urls import path
from API_Weatherstack import views

urlpatterns = [
    path('',views.index),
    path('API_Weatherstack',views.API_Weatherstack)
]