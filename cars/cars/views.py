from django.http import JsonResponse
from .models import Car
from .serializers import CarModel

def get_cars(request):
    cars = Car.objects.all()
    serializer = CarModel(cars, many=True)
    return JsonResponse(serializer.data, safe = False)