from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home2.html',{'name':'Ninad'})

def fs(request):
    return render(request,'demo.html')
