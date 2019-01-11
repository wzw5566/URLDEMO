from django.shortcuts import render
from http.client import responses
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def info(request):
    if request.method=='GET':
        token=request.GET.get('token')
        return HttpResponse("token:" + token )