from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum

from administrator.models import Application, Student, Student_ad_sponsor
from administrator.permission import IssuePermission
from administrator.serializers import ApplicationSerializer, StudentSerializer, Student_sponsorSerializer
from elasticsearch_dsl import Search
from rest_framework.filters import SearchFilter

from spon.models import ArizaHomiy
from spon.serializers import ArizaHomiySerializer
from rest_framework.permissions import AllowAny
from django.db import connection


# Create your views here.
class ApplicationListView(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IssuePermission,)

    filter_backends = (SearchFilter,)
    search_fields = ('title', 'text', 'to_author__username')

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IssuePermission,)
    parser_classes = [MultiPartParser]


class Student_sponsorSet(ModelViewSet):
    queryset = Student_ad_sponsor.objects.all()
    serializer_class = Student_sponsorSerializer
    permission_classes = (IssuePermission,)
    parser_classes = [MultiPartParser]
    http_method_names = ('get','post', 'patch')


@api_view(['GET'])
@permission_classes([AllowAny])
def total_contribution(request):
    total_amount = ArizaHomiy.objects.aggregate(total=Sum('summa'))['total']
    return Response({'total_contribution': total_amount})

@api_view(['GET'])
@permission_classes([AllowAny])
def total_contribution_contract(request):
    total_amount = Student.objects.aggregate(total=Sum('contract'))['total']
    return Response({'total_contribution': total_amount})


@api_view(['GET'])
@permission_classes([AllowAny])
def remaining_contract(request):
    today =    ArizaHomiy.objects.aggregate(total=Sum('summa'))['total'] - Student.objects.aggregate(total=Sum('contract'))['total']
    if today < 0:
        model = abs(today)
        return Response({'qolgan contiractlar': model})
    return Response({'qolgan contiractlar ', today})


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def cponser_homiy(request):
#     request = "select users, phone, person, organization from spon_arizahomiy"
#     return Response({'cponser_homiy': request})


@api_view(['GET'])
@permission_classes([AllowAny])
def cponser_homiy(request):
    sorov = "SELECT id, users, phone, person, organization FROM spon_arizahomiy"

    with connection.cursor() as cursor:
        cursor.execute(sorov)
        results = cursor.fetchall()

    response_data = []
    for i in results:
        data = {
            'id': i[0],
            'users': i[1],
            'phone': i[2],
            'person': i[3],
            'organization': i[4],
        }
        response_data.append(data)

    return Response({'cponser_homiy': response_data})


@api_view(['GET'])
@permission_classes([AllowAny])
def student_key_sponsor(request):
    sorov = (''' SELECT sas.id, sas.id, sa.users AS sponsor_users
                FROM administrator_student_ad_sponsor sas
                INNER JOIN administrator_student s ON sas.id = s.id
                LEFT JOIN spon_arizahomiy sa ON sas.sponsor_id = sa.id;
'''
             )

    with connection.cursor() as cursor:
        cursor.execute(sorov)
        results = cursor.fetchall()

    response_data = []
    for i in results:
        data = {
            'id': i[0],
            'users': i[1],
            'phone': i[2],
        }
        response_data.append(data)

    return Response({'cponser_homiy': response_data})


