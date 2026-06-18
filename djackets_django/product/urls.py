from django.urls import path

from .views import LatestProducts, ProductDetail, CategoryDetail , search

urlpatterns = [
    path('latest-products/', LatestProducts.as_view(), name='latest-products'),
    path('search/', search, name='product-search'),
    path('category/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='product-detail'),
    path( 'category/<slug:category_slug>/', CategoryDetail.as_view(), name='category-detail'),
]