from django.db import models

# Create your models here.
class Article(models.Model):
    # CharField 사용 시 반드시 max_length 인자 필요
    title = models.CharField(max_length=10)
    content = models.TextField()