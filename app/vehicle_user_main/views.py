from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1>Hii Vantedge!<\h1>")

def v1(response):
    return HttpResponse("<h1>VantEdge Terminal Boss Testing 1<\h1>")

