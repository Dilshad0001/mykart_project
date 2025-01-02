
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.productuserview.as_view())
]
