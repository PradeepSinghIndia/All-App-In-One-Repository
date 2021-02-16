from django.urls import path
from MyApp import views

urlpatterns = [
    path('', views.hello ,name='hello'), #this is url of view, name home
]