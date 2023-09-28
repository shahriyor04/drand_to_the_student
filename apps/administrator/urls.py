from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import ApplicationListView

router = DefaultRouter()

router.register('admin_list', ApplicationListView , basename='admin_list')

urlpatterns = [
    path('', include(router.urls)),
    path('total-contribution/', views.total_contribution, name='total_contribution'),
    path('cponser_homiy/', views.cponser_homiy, name='cponser_homiy'),

]
