from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index") , 
    path("contact/",contact,name='contact'),
    path("menu/",menu,name="menu"),
    path("service/",services,name="services"),
    path("about/",about,name='about'),
    #for authentication:
    path("register/",register,name="register"),
    path("log_in/",log_in,name="log_in"),
    path("log_out/",log_out,name="log_out"),
    
         
]