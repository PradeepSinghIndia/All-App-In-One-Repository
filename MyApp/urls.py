from django.urls import path
from MyApp import views

urlpatterns = [
    path('', views.hello ,name='helloword'), #this is url of view, name home
]