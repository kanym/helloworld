from django.shortcuts import render
from django.http import HttpResponse

def homePageView(reguest):
    return HttpResponse("Hello world")

