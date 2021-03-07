from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Mohammad Hasan </h1>")