from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.Serializer):
    category_id =      serializers.IntegerField()
    manufacturer_id =  serializers.IntegerField()
    model_name =    serializers.CharField(max_length=100)
    description =    serializers.CharField(required=False)
    time_created =  serializers.DateTimeField(read_only=True)
    time_updated =  serializers.DateTimeField(read_only=True)
    is_displayed =  serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('model_name', 'manufacturer_id', 'category_id', 'description')