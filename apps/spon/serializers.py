from rest_framework.fields import ChoiceField, CharField
from rest_framework.serializers import ModelSerializer

from .models import Category, ArizaHomiy


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ArizaHomiySerializer(ModelSerializer):
    # payment_type = ChoiceField(choices=['cash', 'card'])
    # organization = CharField(max_length=255)
    class Meta:
        model = ArizaHomiy
        fields = ('category1', 'users', 'phone', 'summa', 'comment', 'payment_type', 'person', 'organization')
