from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework_jwt.utils import jwt_decode_handler
from django.contrib.auth import get_user_model
from users.serializers import UserDetailSerializer



# Create your views here.
def info(request):
    User = get_user_model()
    if request.method=='GET':
        token=request.GET.get('token')
        toke_user = []
        toke_user = jwt_decode_handler(token)
        user_id = toke_user["user_id"]
        user_info = User.objects.get(pk= user_id)
        serializer = UserDetailSerializer(user_info)
        return JsonResponse(serializer.data, status=200)
