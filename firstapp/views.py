from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, 'firstapp/index.html', {})


def ajax(request):
    data = {'name':'Mohammad Hasan', 'age':20, 'mobile':'01862441950'}
    
    response = JsonResponse(data)
    response['Access-Control-Allow-Origin'] = '*'
    return response