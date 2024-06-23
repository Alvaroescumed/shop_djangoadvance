from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    permission_classes = [isClient]

    @action(detail=False, methods=['get'])
    
    def by_category(self, req):
        
        category_id = req.query_params.get('category_id')

        if category_id:
            
            products = Product.objects.filter(category_id=category_id)
            serializer =ProductSerializer(products, many=True)
            return Response(serializer.data)
        
        else: 
            return Response({'error': 'Se requiere proporcionar category_id como parámetro.'}, status=status.HTTP_400_BAD_REQUEST)

        
