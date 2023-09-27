from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationListView
router = DefaultRouter()

router.register('admin_list', ApplicationListView , basename='admin_list')

urlpatterns = [
    path('', include(router.urls)),

]
