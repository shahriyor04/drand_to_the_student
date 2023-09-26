from django.urls import path, include

urlpatterns = [
    path('homiy/', include('spon.urls')),
    path('students/', include('students.urls')),

]
