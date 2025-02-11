from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users import models


# Create your views here.

@api_view(['POST'])
def create_user_api(request):
    # request.method / request.POST
    # request.data
    # return Response()
    if request.method == 'POST':
        user = models.User.objects.create_user(**request.data)
        request.data['id'] = user.pk
        request.data.pop('password')
        return Response(request.data, status=status.HTTP_201_CREATED)
