from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def qrcode(request):
    return render(request,"qr.html")