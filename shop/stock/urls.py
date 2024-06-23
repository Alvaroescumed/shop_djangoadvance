from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='products-list-create'),
    path('products/<int:pk>', ProductDetail.as_view(), name='products-detail'),
    path('category/', CategoryList.as_view(), name='category-list-create'),
    path('category/<int:pk>', CategoryDetail.as_view(), name='category-detail'),
    path('inventory/', InventoryList.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>', InventoryDetail.as_view(), name='inventory-detail'),
    path('catalog/', CatalogListView.as_view(), name='catalog-list')
]