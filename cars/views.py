from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

class CarList(generics.ListAPIView):
    '''
    Show all car info
    '''
    queryset = Car.objects.all()
    serializer_class = CarSerializer

def links(request):
    return render(request, 'cars/links.html')