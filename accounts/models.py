from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender_choices = [
        ('남성', 'M'),
        ('여성', 'F'),
    ]
    nickname = models.CharField(max_length=10, unique=True)
    birthday = models.DateField()
    gender = models.CharField(choices=gender_choices, max_length=2, blank=True)
    email = models.EmailField(unique=True)