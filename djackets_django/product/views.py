from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

from django.http import Http404
# Create your views here.
class LatestProducts(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(available=True).order_by('-created')[:5]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.get(category__slug=category_slug, slug=product_slug)
        except Product.DoesNotExist:
            return Http404
        
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        