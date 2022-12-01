from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from random import randint
import jwt


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=45)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.CharField(max_length=80, unique=True)
    wage = models.DecimalField(max_digits=9, decimal_places=2)
    # Account settings
    agency = models.CharField(max_length=6, editable=False)
    balance = models.DecimalField(max_digits=9, decimal_places=2)


    objects = CustomUserManager()
    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["username", "email", "wage", "password"]

    @property
    def number(self):
        cpf = self.cpf
        number_account = ""
        for i in cpf:
            number_account += i
            if len(number_account) == 7:
                break
        number_account = number_account.replace(".", "0")
        number_final = number_account+"-"+"0"
        return number_final


    @property
    def token(self):
        token = jwt.encode({
            'username':self.username,
            'cpf': self.cpf,
            'email': self.email,
            'wage': str(self.wage),
            'password': self.password,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, settings.SECRET_KEY, algorithm='HS256')

        return token



    def __str__(self):
        return self.username

# class Transference(models.Model):
#     user = models.ForeignKey(User)