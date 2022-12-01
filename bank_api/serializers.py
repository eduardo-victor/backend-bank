from rest_framework import serializers
from .models import *
from random import randint
import decimal


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=6, write_only=True)
    number = serializers.ReadOnlyField()
    agency = serializers.CharField(default='2582-0')
    balance = serializers.DecimalField(max_digits=9, decimal_places=2, default=2000.00)

    class Meta:
        model = User
        fields = ['id', 'username', 'cpf', 'email', 'wage', 'password', 'number', 'agency', 'balance']

    def create(self, validated_data):
        user = User.objects.create_superuser(
            username=validated_data['username'],
            cpf=validated_data['cpf'],
            email=validated_data['email'],
            wage=validated_data['wage'],
            password=validated_data['password'],
            agency=validated_data['agency'],       
            balance=validated_data['balance'],       
        )

        return user
        

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['cpf', 'password', 'token']
        read_only_fields = ['token']