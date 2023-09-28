from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, ArizaHomiySerializer
from .models import Category, ArizaHomiy


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    parser_classes = [MultiPartParser]

    filter_backends = (SearchFilter,)
    search_fields = ('title', 'text', 'to_author__username')


class ArizaHomiyViewSet(ModelViewSet):
    serializer_class = ArizaHomiySerializer
    queryset = ArizaHomiy.objects.all()
    parser_classes = [MultiPartParser]

    filter_backends = (SearchFilter,)
    search_fields = ()
