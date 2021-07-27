from django.shortcuts import render
from django.http import HttpResponse

'''def yamaha(request):
    return HttpResponse("Hi this is App by Sandesh")

def tvs(request):
    return render(request,'home.html')
'''

def home(request):
    return render(request,"op2.html")

def add(request):
    v1 = int(request.GET['no1'])
    v2 = int(request.GET['no2'])
    res = (v1+v2)
    return render(request,"op3.html",{"result":res})
