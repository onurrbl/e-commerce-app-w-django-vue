from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
class LatestProducts(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(available=True).order_by('-created')[:5]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
