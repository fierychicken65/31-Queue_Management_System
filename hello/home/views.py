from django.shortcuts import render,HttpResponse
from .models import persons
# Create your views here.
def index(request):
    return render(request,'index.html')

def qrcode(request):
    return render(request,"qr.html")
def adddata(request):
    records={
        "token":7,
        "now":4,
    }
    persons.insert_one(records)

    return HttpResponse("Done")
def finddata(request):
   records= persons.find()
   
   return HttpResponse(records)