"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from cars.views import links, CarList, CarAPIView, CarViewSet, CarGetOnlyViewSet
from rest_framework import routers

simple_router = routers.SimpleRouter()
simple_router.register(r'car', CarViewSet)
second_router = routers.SimpleRouter()
second_router.register(r'car-data', CarGetOnlyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.2/car/', CarList.as_view(), name='car_list'),
    path('api/v1.2/car/<int:pk>/', CarList.as_view(), name='car_post'),
    path('api/v1.1/car/', CarAPIView.as_view(), name='car_api'),
    path('api/v1.1/car/<int:pk>/', CarAPIView.as_view(), name='car_update'),
    path('api/v1.5/', include(simple_router.urls)),
    # path('api/v1.5/car/', CarViewSet.as_view({'get': 'list'}), name='car_get'),
    # path('api/v1.5/car/<int:pk>/', CarViewSet.as_view({'put': 'update'}), name='car_put'),
    path('api/v1.7/', include(second_router.urls)),
    path('', links, name='links'),
]
