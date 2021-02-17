from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def defaultView(request):
    return HttpResponse("hi blog")
def about(request):
    return HttpResponse("hi blog")