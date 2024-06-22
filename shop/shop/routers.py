from rest_framework.routers import DefaultRouter
from stock.viewsets import *

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
urlpatterns = router.urls