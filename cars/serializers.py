from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.Serializer):
    category_id =      serializers.IntegerField()
    manufacturer_id =  serializers.IntegerField()
    model_name =    serializers.CharField(max_length=100)
    description =    serializers.CharField()
    time_created =  serializers.DateTimeField()
    time_updated =  serializers.DateTimeField()
    is_displayed =  serializers.BooleanField(default=True)

    
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('model_name', 'manufacturer_id', 'category_id', 'description')