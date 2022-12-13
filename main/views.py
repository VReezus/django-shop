from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from .filters import ProductFilter 

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class=ProductFilter
    # filterset_fields = ['category', 'status']
    # permission_classes = [AllowAny, ]

    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            return []#если это запрос на листинг или детализацию
        return [IsAdminUser()] #разрешаем всем
        
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])


    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        if q:
            queryset=queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        # queryset = Product.objects.filter(title__icontains=q)
        pagination = self.paginate_queryset(queryset)
        
        if pagination:
            serializer=self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer=self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)




