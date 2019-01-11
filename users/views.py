from django.shortcuts import render
from django.http import HttpResponse
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework_jwt.utils import jwt_response_payload_handler

# Create your views here.
def info(request):
    if request.method=='GET':
        token=request.GET.get('token')
        user = []
        user = jwt_decode_handler(token)
        user_id = user["user_id"]
        return HttpResponse(user_id )