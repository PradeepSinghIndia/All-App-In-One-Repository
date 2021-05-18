from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from shop.serializers import ProductSerializer
from shop.models import Product

# create our own pagination class
class ProductPagination(LimitOffsetPagination):
    defualt_limit=10
    max_limit=100

class ProductList(ListAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer
    filter_backends=(DjangoFilterBackend,SearchFilter)
    filter_fields=('product_name',)
    search_fields=('product_name','desc')
    pagination_class=ProductPagination

# create a new product using API    
class ProductCreate(CreateAPIView):
    serializer_class=ProductSerializer
    # override the create method
    def create(self, request, *args, **kwargs):
        try:
            price=request.data.get('price')
            # this validation will stop creating product for free accidently
            if price is not None and float(price)<=0.0:
                raise ValidationError({'price':'must be above $0.0'})
        except ValueError: #if parsing the price doe'nt work
            raise ValidationError({'price':'A valid number is required'})
        return super().create(request, *args, **kwargs)    
"""
#api for deleting product from database        
class ProductDestroy(DestroyAPIView):
    queryset=Product.objects.all()
    lookup_field='id'
    # clear the cache for other objects to be use the space
    def delete(self, request, *args, **kwargs):
        product_id=request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code==204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response    
"""
#api for retrieve, delete, and upadate product        
class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    lookup_field='id'
    serializer_class=ProductSerializer
    # clear the cache for other objects to be use the space
    def delete(self, request, *args, **kwargs):
        product_id=request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code==204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response  
    def update(self, request, *args, **kwargs):

        response=super().update(request, *args, **kwargs)
        if response.status_code==200:
            from django.core.cache import cache
            product=response.data
            cache.set('product_data_{}'.format(product['id']),{
                'product_name':product['product_name'],
                'desc':product['desc'],
                'price':product['price'],
                'pub_date':product['pub_date'],

            }) 
        return response    
