from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Model, ForeignKey, CASCADE, BooleanField, OneToOneField, CharField, IntegerField, TextField
from rest_framework.exceptions import ValidationError

from spon.models import ArizaHomiy


class Application(Model):
    user = OneToOneField(ArizaHomiy, on_delete=CASCADE, primary_key=True)
    is_approved = BooleanField(default=False)

    def __str__(self):
        return self.user.users


def is_valid_username(username):
    parts = username.split()
    if len(parts) < 3:
        raise ValidationError("Username should have at least 3 parts.")


def phone_number(number):
    number = RegexValidator(
        regex=r'^\d{9}$',
        message="Phone number must be exactly 9 digits long.",
    )
    raise ValidationError("Phone number must be exactly 9 digits")


class Student(Model):
    username = CharField(max_length=250, validators=[is_valid_username])
    phone = IntegerField(validators=[phone_number])
    OTM = CharField(max_length=255)
    type_student = CharField(max_length=255)
    contract = IntegerField()

    def __str__(self):
        return self.username


class Student_ad_sponsor(Model):
    student = ForeignKey(Student, on_delete=CASCADE)
    sponsor = ForeignKey(ArizaHomiy, on_delete=CASCADE)

    def __str__(self):
        return f"{self.student.username} - {self.sponsor.users}"

    def Sonni(self):
        student_username = self.student.username if self.student else "N/A"
        sponsor_username = self.sponsor.users if self.sponsor else "N/A"
        return f"Student Username: {student_username} - Sponsor Username: {sponsor_username}"
