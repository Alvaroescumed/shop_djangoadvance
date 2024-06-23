from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import *

# ------ Vies de Productos --------

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [isClient]

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [isClient]

# ---- Vistas Categoria ---------

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ------ Vistas Inventario ---------

class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [isGerente]

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


# --------APIVIEWS---------

class ProductWithInventory(APIView):
    def get(self, req):

        products = Product.objects.all()
        produc_serializer= ProductSerializer(products, many=True)
        data=[]

        for product_data in produc_serializer:
            try: 
                inventory = Inventory.objects.get(product_id=product_data['id'])
                inventory_data = InventorySerializer(inventory).data
                product_data['inventory_quantity'] = inventory_data['quantity']
            except Inventory.DoesNotExist:
                product_data['inventory_quantity'] = 0

            data.append(data)
        return Response(data)