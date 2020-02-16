
from django.shortcuts import render
#from  . weather import x
import requests, json 

def index(request):

   
    data="welcome"
    return render(request,'index.html',{'data':data})
