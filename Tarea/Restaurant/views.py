#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Hamburgesa, Ingrediente
from .serializers import HamburgesaSerializer, IngredienteSerializer


def index(request):
    return HttpResponse("Vista index del restaurante")

@api_view(['GET', 'POST'])
def hamburgesas(request, formato=None):
    
    if request.method == 'GET':
        hamburgesas = Hamburgesa.objects.all()
        serializer = HamburgesaSerializer(hamburgesas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HamburgesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def ingredientes(request, formato=None):
    
    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def ingrediente_id(request, pk, formato=None):
    
    try:
        ingrediente = Ingrediente.objects.get(pk=pk)
    except Ingrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PATCH', 'DELETE']) #Ver si PATCH esta correcto
def hamburgesa_id(request, pk, formato=None):
    
    try:
        hamburgesa = Hamburgesa.objects.get(pk=pk)
    except Hamburgesa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HamburgesaSerializer(hamburgesa)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        hamburgesa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH': #Revisar
        serializer = HamburgesaSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)