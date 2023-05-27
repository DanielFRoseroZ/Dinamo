from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, get_object_or_404
from rest_framework.decorators import api_view 
from .serializer import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def register(request):
    try:
        serializer = User_serializer(data = request.data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except BaseException:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def register(request):
    try:
        serializer = Rol_serializer(data = request.data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except BaseException:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    try:
        serializer = Sucursal_serializer(data = request.data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except BaseException:
        return Response(status=status.HTTP_400_BAD_REQUEST)