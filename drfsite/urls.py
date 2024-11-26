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
from cars.views import CarUpdate, CarDestroy, CarToken, CarJWToken, CarCategoryList
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

simple_router = routers.DefaultRouter()
simple_router.register(r'car', CarViewSet, basename='default-car')
second_router = routers.SimpleRouter()
second_router.register(r'car-data', CarGetOnlyViewSet)
# for e in simple_router.urls:
#     print(e)

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
    path('api/v1.8/car/<int:pk>/', CarUpdate.as_view(), name='car_update_perms'),
    path('api/v1.8/cardelete/<int:pk>/', CarDestroy.as_view(), name='car_delete_perms'),
    # The token authentication provided by Django REST framework
    path('api/v1.12/car/<int:pk>/', CarToken.as_view(), name='car_token_auth'),
    path('api/v1.14/car/<int:pk>/', CarJWToken.as_view(), name='car_jwt_auth'),
    path('api/v1.15/car_categories/', CarCategoryList.as_view(), name='car_categories'),
    path('', links, name='links'),
    
    # uses Django's default session backend for authentication
    path('api/v1.11/drf-auth/', include('rest_framework.urls')),
    
    # The obtain_auth_token view will return a JSON response
    # when valid username and password fields are POSTed to the view using form data or JSON
    path('api-token-auth/', views.obtain_auth_token), # POST

    #  Simple JWT JSON Web Token authentication backend for the Django REST Framework
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

    # AssertionError: .accepted_renderer not set on Response
    # path('api/v1.12/get-token/', get_token, name='get_token'),
