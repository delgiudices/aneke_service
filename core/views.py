from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        if self.request.query_params:
            filter_params = {}
            for k, v in self.request.query_params.items():
                filter_params[k] = v
            return Product.objects.filter(**filter_params)
        else:
            return Product.objects.all()
