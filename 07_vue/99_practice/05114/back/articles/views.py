# articles/views.py

from django.shortcuts import render, get_object_or_404
from .models import Article
from .serializer import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def index(request):
    # Article 모델에 있는 모든 인스턴스 가져오기
    articles = Article.objects.all()
    # ArticleSerializer를 사용해서 articles(Article의 모든 인스턴스를 담은 변수)를 직렬화
    serializer = ArticleSerializer(articles, many=True)
    # Response를 사용해서 serializer로 직렬화한 데이터를 반환
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    # ArticleSerializer데이터에 요청 데이터를 넣어 직렬화
    serializer = ArticleSerializer(data=request.data)
    # 유효성 검사를 통과하지 못하면 오류 반환
    if serializer.is_valid(raise_exception=True):
        # 유효성 검사 통과 시 저장, serializer의 데이터 반환
        serializer.save()
        return Response(serializer.data)
    
@api_view(['PUT'])    # 수정은 무조건 PUT 사용
def update(request, article_pk):
    # article 변수에 수정할 pk를 가진 인스턴스를 찾아서 가져오기
    article = get_object_or_404(Article, pk=article_pk)
    # 요청 데이터를 넣어 직렬화, article을 넣어 그 인스턴스의 내용을 수정
    serializer = ArticleSerializer(article, data=request.data)
    # 수정한 내용 유효성 검사하기 -> 통과 시 저장
    if serializer.is_valid(raise_exception=True):
        serializer.save()

        return Response(serializer.data)

@api_view(['DELETE'])    # 삭제는 무조건 DELETE 사용
def delete(request, article_pk):
    # 삭제할 pk를 가진 데이터 가져와 article 변수에 저장, 삭제
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()

    # views.py에서 데이터를 넘기고 싶다면 context에 담아서 전달
    # context={
    #     'deleted_instance':article.pk
    # }
    # return Response(context,status=status.HTTP_204_NO_CONTENT)

    # 삭제 후 해당 내용이 없다는 HTTP 상태 반환
    return Response(status=status.HTTP_204_NO_CONTENT)