from django.http import JsonResponse
from .models import Car
from .serializers import CarModel
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST']) #here ap_view is a decorator
def get_cars(request): 
    if request.method == 'GET':
       cars = Car.objects.all()
       serializer = CarModel(cars, many=True)
       return Response(serializer.data)
    if request.method == 'POST':
        serializer  = CarModel(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def get_car(request,id):
    try:
        car = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CarModel(car)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CarModel(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)