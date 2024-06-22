from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=False, methods=['get'])
    
    def by_category(self, req):
        category_id = req.query_params.get('category_id')

        if category_id:
            
            products = Product.objects.filter(category_id=category_id)
        
        else: 
            products = Product.objects.all()

        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
