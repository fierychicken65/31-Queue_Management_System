from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    #path("", views.index, name = 'home'),
    path("",views.adddata,name="adddata"),
    path("qrcode",views.qrcode, name = 'qrcode'),
    path("del",views.deleteall,name="finddata")
]