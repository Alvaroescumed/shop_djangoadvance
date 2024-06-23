from rest_framework import serializers
from .models import * 

class ProductSerializer(serializers.ModelSerializer):

    # ausamos el nombre de la categoria en vez de el idw
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.name
        return representation

    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'