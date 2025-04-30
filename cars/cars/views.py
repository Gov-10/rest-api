from django.http import JsonResponse
from .models import Car
from .serializers import CarModel
from rest_framework.decorators import api_view

@api_view(['GET', 'POST']) #here ap_view is a decorator
def get_cars(request): 
    if request.method == 'GET':
       cars = Car.objects.all()
       serializer = CarModel(cars, many=True)
       return JsonResponse(serializer.data, safe = False)
    if request.method == 'POST':
        serializer  = CarModel(data = request.data)
        