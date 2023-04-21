from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    # actors 괄호 속 내용 확인
    
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    
# 관계를 기억해주는 중개모델 생성
# class Movie_Actors(models.Model):
#     Actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
#     Movie = models.ForeignKey(Movie, on_delete=models.CASCADE)