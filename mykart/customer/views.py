from django.shortcuts import render
from rest_framework.views import APIView
from .models import product
from .serializers import productserialiser
from rest_framework.response import Response

# Create your views here.



class productuserview(APIView):
    def get(serlf,request):
        obj=product.objects.all()
        ser=productserialiser(obj, many=True)
        return Response(ser.data)