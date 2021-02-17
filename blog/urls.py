from django.urls import path
from blog import views

urlpatterns = [
    path('' ,views.defaultView ,name='default'),
    path('about/' ,views.about ,name='about'),
    

]