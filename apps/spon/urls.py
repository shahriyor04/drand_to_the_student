from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ArizaHomiyViewSet
router = DefaultRouter()

router.register('category', CategoryViewSet , basename='sponsor')
router.register('ariza', ArizaHomiyViewSet , basename='ariza')

urlpatterns = [
    path('', include(router.urls)),

]
