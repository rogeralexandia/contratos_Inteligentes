from rest_framework import serializers

from core.pos.models import Category, Product


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        return instance.toJSON()
