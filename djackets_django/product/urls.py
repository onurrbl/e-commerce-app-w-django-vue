from django.urls import path

from .views import LatestProducts, ProductDetail

urlpatterns = [
    path('latest-products/', LatestProducts.as_view(), name='latest-products'),
    path('category/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='product-detail'),
]