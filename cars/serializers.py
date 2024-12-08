from rest_framework import serializers
from .models import Car, Category, Manufacturer

class CarSerializer(serializers.Serializer):
    # fields =  ['category_id', 'manufacturer_id', 'model_name', 'description', 'time_created', 'time_updated', 'is_displayed']
    category_id =      serializers.IntegerField()
    manufacturer_id =  serializers.IntegerField()
    model_name =    serializers.CharField(max_length=100)
    description =    serializers.CharField(required=False)
    time_created =  serializers.DateTimeField(read_only=True)
    time_updated =  serializers.DateTimeField(read_only=True)
    is_displayed =  serializers.BooleanField(default=True)

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.manufacturer_id = validated_data.get("manufacturer_id", instance.manufacturer_id)
        instance.model_name = validated_data.get("model_name", instance.model_name)
        instance.description = validated_data.get("description", instance.description)
        # instance.time_created = validated_data.get("time_created", instance.time_created)
        # instance.time_updated = validated_data.get("time_updated", instance.time_updated)
        instance.is_displayed = validated_data.get("is_displayed", instance.is_displayed)
        instance.save()
        return instance
    


class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'definition')


class CarManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'brand', )


class CarModelSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # The field 'owner' was declared on serializer CarModelSerializer, but has not been included in the 'fields' option.
    # manufacturer = CarManufacturerSerializer()
    # category = CarCategorySerializer()
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title',
        )
    manufacturer = serializers.StringRelatedField(many=False)


    class Meta:
        model = Car
        # fields = "__all__"
        fields = ('id', 'owner', 'model_name', 'manufacturer', 'category', 'description', 'is_displayed')
