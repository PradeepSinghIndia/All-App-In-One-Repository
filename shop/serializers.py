from rest_framework import serializers
from shop.models import Product
from rest_framework.renderers import JSONRenderer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= ('id','product_name','desc','price','pub_date')

    def to_representation(self,instance):
        data=super().to_representation(instance)
        data['current_price']=instance.price 
        return data   
