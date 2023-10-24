from django.apps import apps
from django.core.validators import RegexValidator, MinValueValidator
from django.db.models import Model, CharField, ForeignKey, IntegerField, TextField, DateTimeField, CASCADE, \
    DecimalField, BooleanField
from django.forms import ChoiceField
from rest_framework.exceptions import ValidationError

categories = [
    ('homiy', 'Homiy '),

]


class Category(Model):
    name = CharField(choices=categories, max_length=20)

    def __str__(self):
        return self.name


def summa_regex(value):
    if value < 500000:
        raise RegexValidator("The amount must not be less than 500,000.")


class ArizaHomiy(Model):
    CHOICES = (
        ('cash', 'Cash'),
        ('card', 'Card'),
    )
    phone_regex = RegexValidator(
        regex=r'^\d{9}$',
        message="Phone number must be exactly 9 digits long.",
    )
    summa_regex = RegexValidator(
        regex='500000',
        message="minimum 500 000 digits"
    )

    category1 = ForeignKey(Category, on_delete=CASCADE)
    users = CharField('I, F, SH', max_length=250)
    phone = IntegerField(validators=[phone_regex])
    summa = DecimalField(max_digits=10, decimal_places=2, validators=[summa_regex])
    payment_type = CharField(max_length=20, choices=CHOICES)
    person = BooleanField(
        default=False

    )
    organization = CharField(max_length=255, blank=True)
    comment = TextField()
    created_at = DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.person:
            self.organization = ''
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.users
