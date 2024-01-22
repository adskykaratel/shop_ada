from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializer import ProductSerializer
from .permissions import IsAuthor
from rest_framework import permissions 
from rest_framework.decorators import action
from rating.serializer import RatingSerializer
from rest_framework.response import Response
import logging
from django.views.decorators.cache import cache_page
from django.core.cache import cache
logger = logging.getLogger(__name__)



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsAuthor(),)
        return(permissions.IsAuthenticatedOrReadOnly(),)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    
    @action (['GET', 'POST', 'DELETE'], detail=True)
    @cache_page(60)
    def ratings(self, request, pk):
        product = self.get_object()
        user = request.user

        if request.method == 'GET':
            rating = product.ratings.all()
            serializer = RatingSerializer(instance=rating, many=True)
            logger.info(f'Get request for ratings of product {pk} by user {user}')
            return Response (serializer.data, status=200)
        
        elif request.method =='POST':
            if product.ratings.filter(owner=user).exists():
                return Response('Ты уже поставил рейтинг на этот товар ? ', status=400)
            serializer = RatingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner = user , product=product)
            return Response(serializer.data, status=201)
        
        else:
            if not product.ratings.filter(owner=user).exists():
                return Response('Ты не можешь удалить потому что ты не оставлял отзыв', status=400)
            rating = product.ratings.get(owner=user)
            rating.delete()
            return Response('Успешно удалено',  status=204)
        