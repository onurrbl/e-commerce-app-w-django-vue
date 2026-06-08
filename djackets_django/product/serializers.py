from rest_framework import serializers
from .models import Product , Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
    

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    image = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'slug', 'description', 'price', 'image', 'thumbnail', 'available', 'created', 'updated','get_absolute_url']
    
    def get_image(self, obj):
        return obj.getImage()
    
    def get_thumbnail(self, obj):
        return obj.getThumbnail()