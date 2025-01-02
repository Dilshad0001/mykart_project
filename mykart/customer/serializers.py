from rest_framework import serializers
from .models import product


class productserialiser(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=['product_name','product_price','product_rating','product_image','product_description','category']


