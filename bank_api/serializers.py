from rest_framework import serializers
from .models import *
from random import randint
import decimal


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=6, write_only=True)
    agency = serializers.CharField(default='2582-0')

    class Meta:
        model = User
        fields = ['id', 'username', 'cpf', 'email', 'wage', 'password', 'agency']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            cpf=validated_data['cpf'],
            email=validated_data['email'],
            wage=validated_data['wage'],
            password=validated_data['password'],
            agency=validated_data['agency'],
        )

        return user
        

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['cpf', 'password', 'token']
        read_only_fields = ['token']