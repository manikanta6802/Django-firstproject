from django.shortcuts import render
from django.http import HttpResponse
def display(request):
    s = '<h1>Hello Students Welcome To Mahesh Sir Django CLasses</h1>'
    return HttpResponse(s)
# Create your views here.
