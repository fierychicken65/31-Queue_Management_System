from django.db import models
import pymongo
uri = "mongodb+srv://aadiudu:scared2compile@scared2compile.wxkvott.mongodb.net/?retryWrites=true&w=majority"
client=pymongo.MongoClient(uri)
db=client['test_mongo']
# Create your models here.
persons=db['persons']