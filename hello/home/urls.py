from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("qrcode",views.qrcode, name = 'qrcode'),
    path("data",views.adddata,name="adddata"),
    path("find",views.finddata,name="finddata")
]