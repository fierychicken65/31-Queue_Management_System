from django.shortcuts import render,HttpResponse
from .models import persons
token=1
pos=1
# Create your views here.
def index(request):
    return render(request,'index.html')

def qrcode(request):
    return render(request,"qr.html")
def adddata(request):
    # Check if the user has already inserted a record
    if 'has_inserted' not in request.session:
        records2 = list(persons.find({}, {'_id': False}))
        token = 1 + len(records2)
        pos = 1 + len(records2)
        records = {
            "token": token,
            "now": pos,
        }
        persons.insert_one(records)

        # Set a session variable to indicate that the user has inserted a record
        request.session['has_inserted'] = True

    # Get the last inserted token from the database
    records2 = list(persons.find({}, {'_id': False}))
    last_record = records2[-1] if records2 else None
    last_token = last_record.get("token") if last_record else None

    message = {
        "message": last_token
    }
    return render(request, "index.html", message)
def deleteall(request):
   persons.drop()
   return HttpResponse("done")