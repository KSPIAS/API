from django.urls import path
from covid import views

urlpatterns = [
    path('',views.API_COVID),
]