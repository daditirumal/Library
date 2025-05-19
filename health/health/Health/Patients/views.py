from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def person(request):
    return HttpResponse("hello world")
def python_first_app(request):
    return HttpResponse("congrats")