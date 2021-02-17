from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def defaultView(request):
    return render(request,'shop/index.html')
def about(request):
    return HttpResponse("about shop")
def contacts(request):
    return HttpResponse("about contacts") 
def search(request):
    return HttpResponse("about seraching items")       
def product(request):
    return HttpResponse("about particular products")
def tracker(request):
    return HttpResponse("about tracking products")
def checkout(request):
    return HttpResponse("about checkouts")        