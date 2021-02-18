from django.urls import path
from shop import views

urlpatterns = [
    path(''  ,views.home ,name='home'),
    path('about/' ,views.about ,name='aboutus'),
    path('contacts/' ,views.contacts ,name='contactus'), 
    path('search/' ,views.search ,name='search'),
    path('productView/' ,views.productView ,name='productview'), 
    path('tracker/' ,views.tracker ,name='tracking'), 
    path('checkout/' ,views.checkout ,name='checkout'),  

]