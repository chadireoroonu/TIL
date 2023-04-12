from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # symmetrical -> 일방향적인 팔로우 기능
    # related_name -> 향후 편의성
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
