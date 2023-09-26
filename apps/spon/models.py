from django.apps import apps
from django.db.models import Model, CharField, ForeignKey, IntegerField, TextField, DateTimeField, CASCADE, DecimalField
from django.forms import ChoiceField

categories = [
    ('homiy', 'Homiy '),

]


class Category(Model):
    name = CharField(choices=categories, max_length=20)

    def __str__(self):
        return self.name


class ArizaHomiy(Model):
    CHOICES = (
        ('cash', 'Cash'),
        ('card', 'Card'),
    )
    category1 = ForeignKey(Category, on_delete=CASCADE)
    users = CharField('I, F, SH', max_length=250)
    phone = IntegerField()
    summa = DecimalField(max_digits=10, decimal_places=2)
    payment_type = CharField(max_length=20, choices=CHOICES)
    comment = TextField()

    def __str__(self):
        return self.users