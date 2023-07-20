from .models import Product
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, ProductDetailSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permisssions_class = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('image'))
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return self.serializer_class
    