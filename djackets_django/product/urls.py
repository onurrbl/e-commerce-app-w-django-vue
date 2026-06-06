from django.urls import path

from .views import LatestProducts

urlpatterns = [
    path('latest-products/', LatestProducts.as_view(), name='latest-products'),
]