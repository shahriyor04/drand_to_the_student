from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, ArizaHomiySerializer
from .models import Category, ArizaHomiy


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    parser_classes = [MultiPartParser]


class ArizaHomiyViewSet(ModelViewSet):
    serializer_class = ArizaHomiySerializer
    queryset = ArizaHomiy.objects.all()
    parser_classes = [MultiPartParser]
