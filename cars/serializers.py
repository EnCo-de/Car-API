from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('model_name', 'manufacturer_id', 'category_id', 'descripion')