from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def greet (request):
    # return HttpResponse("<h1> HELLO GUYS </h1")
    return render(request,'home.html',{'name':'python'})

def add(request):
    val1 = int(request.POST['number 1'])
    val2 = int(request.POST['number 2'])
    res = val1 + val2
    return render(request,'result.html',{'result':res})