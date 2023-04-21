# 07_pjt

## settings.py

- INSTALLED_APPS =['appname', 'rest_framework',] 추가하기

## project/urls

- path('api/v1/', include('appname.urls') 

## models.py

- 중개모델 생성 : 필요하면 만들기
  
  ```python
  class Movie_Actors(models.Model):
      Actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
      Movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  ```

- MTMF : 중개모델 굳이 안만들어도 될때
  
  ```python
  class Movie(models.Model):
      actors = models.ManyToManyField(Actor, related_name='movies')
  ```
  
  - related_name=' ' : 설정 시 이름 사용 가능
  
  - related_name=' ' : 미설정 시 (serializer) actor 에서 movie 부르면 movie_set

## serializers.py

- fields 요소 한 개일 때도 콤마 반드시 찍기
  
  ```python
  class MovieTitleSerializer(serializers.ModelSerializer):
      class Meta:
          model = Movie
          fields = ('title',) # 콤마 생략 불가
  ```

- 다른 serializer 요소 받아올 때(받아올 요소 많음)
  
  ```python
  class ActorDetailSerializer(serializers.ModelSerializer):
      movies = MovieTitleSerializer(many=True, read_only=True)
      class Meta:
          model = Actor
          fields = '__all__'
  ```
  
  - many는 받아오는 요소가 많을 때
  
  - movies는 설정 이름 사용
  
  - 이름 미설정 시, actor 에서 movie 부르면 movie_set

- 다른 serializer 요소 받아올 때(받아올 요소 한 개)
  
  ```python
  class ReviewDetailSerializer(serializers.ModelSerializer):
      # models의 movie 키워드로 movieTitleSerializer 키 맞는거 하나 가져와
      # 모델 안에 관계 맺고 있는 거 이름이 있으니까
      # 없으면 배우상세처럼 들고와야함
      movie = MovieTitleSerializer(read_only=True)
      class Meta:
          model = Review
          fields = '__all__'
  ```

## views.py

- 백지 상태에서 코드 떠올리는 데에 어려움 -> 꼼꼼히 읽어보기
  
  ```python
  from django.shortcuts import get_object_or_404, get_list_or_404
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  from rest_framework import status
  
  from .models import Actor, Movie, Review
  from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer, ActorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer
  
  # Create your views here.
  @api_view(['GET'])
  def actor_list(request):
      actors = Actor.objects.all()
      serializer = ActorSerializer(actors, many=True)
      return Response(serializer.data)
  
  @api_view(['GET', 'PUT', 'DELETE'])
  def review_detail(request, review_pk):
      reviews = get_object_or_404(Review, pk=review_pk)
  
      if request.method == 'GET':
          serializer = ReviewDetailSerializer(reviews)
          return Response(serializer.data)
  
      elif request.method == 'PUT':
          serializer = ReviewSerializer(reviews, data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
  
      elif request.method == 'DELETE':
          reviews.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
  
  @api_view(['POST'])
  def create_review(request, movie_pk):
      movie = get_object_or_404(Movie, pk=movie_pk)
  
      serializer = ReviewSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(movie=movie)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
  ```
