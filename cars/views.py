from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly

from .models import Car, Category
from .serializers import CarSerializer, CarModelSerializer
from .permissions import IsOwnerOrReadOnly

class CarViewSet(viewsets.ModelViewSet):
    # queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Car.objects.filter(pk=self.kwargs.get('pk'))
        return Car.objects.order_by('-id')[:3]
    
    @action(methods=['get'], detail=False)
    def categories(self, request):
        categories = Category.objects.all()
        return Response({'categories': [{'title': c.title, 'definition': c.definition} for c in categories]})
    
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        js = {'error': '400 Bad request'}
        if pk is not None:
            category = Category.objects.filter(car__id=pk)
            if category.exists():
                js = {'categories': {'title': category[0].title, 'definition': category[0].definition}}
        return Response(js)



class CarGetOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIView(APIView):
    '''
    Uses rest_framework.views.APIView class with rest_framework.serializers.Serializer
    '''
    def get(self, request):
        qs = Car.objects.all()
        return Response({'posts': CarSerializer(qs, many=True).data})
    
    def post(self, request):
        print(request.method, request.data)
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

        # new_car = Car.objects.create(
        #     category_id=request.data['category_id'],
        #     manufacturer_id=request.data['manufacturer_id'],
        #     model_name=request.data['model_name'],
        #     description=request.data.get('description', '')
        # )
        # return Response({'post': CarSerializer(new_car).data})

    def put(self, request, *args, **kwargs):
        print(request.method, request.data)
        if not 'pk' in kwargs:
            return Response({'error': 'Method PUT not allowed'})
        try:
            pk = kwargs['pk']
            instance = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response({'error': 'Object does not exist'})
        serializer = CarSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'put': serializer.data})

    def delete(self, request, *args, **kwargs):
        print(request.method, request.data)
        if not 'pk' in kwargs:
            return Response({'error': 'Method DELETE is not allowed without item number'})
        try:
            pk = kwargs['pk']
            number, deleted = Car.objects.get(pk=pk).delete()
            print('\t', pk, number, deleted)
        except Car.DoesNotExist:
            return Response({'error': 'Object does not exist'})
        return Response({'delete': {'pk': pk, 'number': number, 'items': deleted}})


class CarList(generics.ListCreateAPIView):
    '''
    Show all car info
    '''
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CarUpdate(generics.RetrieveUpdateAPIView):
    '''Permission required to update car info'''
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CarDestroy(generics.DestroyAPIView):
    '''Only Admin can delete cars'''
    queryset = Car.objects.all()
    # serializer_class = CarModelSerializer
    permission_classes = (IsAdminUser, )


def links(request):
    return render(request, 'cars/links.html')