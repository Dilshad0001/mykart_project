from django.shortcuts import render
from rest_framework.views import APIView
from .models import product
from .serializers import productserialiser
from rest_framework.response import Response
from django.db.models import Q


# <---user registration--->
from .serializers import Regserializer

class UserReg(APIView):
    def post(self,request):
        user_data=request.data
        serialiser=Regserializer(data=user_data)
        if serialiser.is_valid():
            serialiser.save()
            return Response('registration compleeted')
        return Response(serialiser.errors)



# <--user login--->
from . models import Customer_data

from .serializers import LogSerializer 

class Userlog(APIView):
    def post(self, request):
        user_data = request.data
        ser = LogSerializer(data=user_data)  
        if not ser.is_valid():
            return Response(ser.errors, status=400)

        enterd_username = ser.validated_data["username"]
        enterd_password = ser.validated_data["password"]
        user=Customer_data.objects.filter(username=enterd_username).first()
        if user is None:
            return Response({'message': 'User does not exist'}, status=404)
        if not user.check_password(enterd_password):
            return Response ('enterd wrong password')
        return Response({'message': 'User exists'}, status=200)



class productuserview(APIView):
    def get(serlf,request):
        keyword=request.GET.get('keyword')
        if keyword:
            obj=product.objects.filter(Q(product_name__startswith=keyword)|Q(category__category_name__startswith=keyword))
        else: 
            obj=product.objects.all()
        ser=productserialiser(obj, many=True)
        return Response(ser.data)