from django.shortcuts import render
from django.http import HttpResponse

def yamaha(request):
    return HttpResponse("Hi this is App by Sandesh")

def tvs(request):
    return render(request,'app_Sandesh.html')