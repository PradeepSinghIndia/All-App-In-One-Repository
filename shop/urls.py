from django.urls import path
from shop import views

urlpatterns = [
    path(''  ,views.defaultView ,name='default'),
    path('about/' ,views.about ,name='about'),
    path('contacts/' ,views.contacts ,name='contacts'), 
    path('search/' ,views.search ,name='search'),
    path('product/' ,views.product ,name='product'), 
    path('tracker/' ,views.tracker ,name='tracker'), 
    path('checkout/' ,views.checkout ,name='checkout'),  

]