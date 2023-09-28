from rest_framework.serializers import ModelSerializer

from administrator.models import Application, Student, Student_ad_sponsor


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class Student_sponsorSerializer(ModelSerializer):
    class Meta:
        model = Student_ad_sponsor
        fields = ('sponsor',)


