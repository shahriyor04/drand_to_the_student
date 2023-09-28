from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import ApplicationListView, StudentViewSet, Student_sponsorSet

router = DefaultRouter()

router.register('admin_list', ApplicationListView , basename='admin_list')
router.register('admin_student', StudentViewSet , basename='admin_student')
router.register('admin_student_ad_sponsor', Student_sponsorSet , basename='admin_student_ad_sponsor')


urlpatterns = [
    path('', include(router.urls)),
    path('total-contribution/', views.total_contribution, name='total_contribution'),
    path('cponser_homiy/', views.cponser_homiy, name='cponser_homiy'),
    path('student_sponsori/', views.student_key_sponsor, name='student_sponsori'),
    path('student_jami_contiract/', views.total_contribution_contract, name='student_sponsori'),
    path('qolgan_contract/', views.remaining_contract, name='qolgan_contract'),

]
