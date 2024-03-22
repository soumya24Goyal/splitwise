from rest_framework import serializers
from .models import User, Split, EqualExpense

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','contact_number']

class SplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Split
        fields = ['id', 'user', 'amount']

class EqualExpenseSerializer(serializers.ModelSerializer):
    splits = SplitSerializer(many=True, read_only=True)

    class Meta:
        model = EqualExpense
        fields = ['id', 'amount', 'paid_by', 'splits']
