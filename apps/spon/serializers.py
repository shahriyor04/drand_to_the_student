from rest_framework.fields import ChoiceField
from rest_framework.serializers import ModelSerializer

from .models import Category, ArizaHomiy


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ArizaHomiySerializer(ModelSerializer):
    # payment_type = ChoiceField(choices=['cash', 'card'])

    class Meta:
        model = ArizaHomiy
        fields = ('category1', 'users', 'phone', 'summa', 'comment', 'payment_type')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['payment_type'] = instance.get_payment_type_display()
        return data
