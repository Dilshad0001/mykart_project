
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.productuserview.as_view()),
    path('reg/',views.UserReg.as_view()),
    path('log/',views.Userlog.as_view())
    
]
