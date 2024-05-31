from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Car
from .serializers import CarSerializer, CarModelSerializer

class CarAPIView(APIView):
    '''
    Uses rest_framework.views.APIView class with rest_framework.serializers.Serializer
    '''
    def get(self, request):
        qs = Car.objects.all()
        return Response({'posts': CarSerializer(qs, many=True).data})
    
    def post(self, request):
        print(request.data)
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_car = Car.objects.create(
            category_id=request.data['category_id'],
            manufacturer_id=request.data['manufacturer_id'],
            model_name=request.data['model_name'],
            description=request.data.get('description', '')
        )
        return Response({'posts': CarSerializer(new_car).data})


class CarList(generics.ListAPIView):
    '''
    Show all car info
    '''
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer


def links(request):
    return render(request, 'cars/links.html')