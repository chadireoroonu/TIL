from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework.response import Response
# 한 번 더 연습해보기
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET'])
def index(request):
    # Article 모델의 모든 인스턴스 article 변수에 담기
    article = Article.objects.all()
    # article 내용을 ArticleSerializer로 직렬화, 여러 개
    serializer = ArticleSerializer(article, many=True)
    # serializer의 데이터 반환
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    # ArticleSerializer에 요청 데이터를 넣어 직렬화
    serializer = ArticleSerializer(data=request.data)
    # 유효성 검사 후 실패 시 오류 반환
    if serializer.is_valid(raise_exception=True):
        # 유효성 검사 통과 시 저장, 제이슨 파일 반환
        serializer.save()
        return Response(serializer.data)
    
@api_view(['PUT'])
def update(request, article_pk):
    # Article 인스턴스 중 요청 pk와 같은 pk를 가진 인스턴스 하나 찾아 변수에 저장
    # 요청 pk와 pk가 일치하는 인스턴스가 없으면 오류 반환
    article = get_object_or_404(Article, pk=article_pk)
    # article에 요청 데이터를 넣어 직렬화
    serializer = ArticleSerializer(article, data=request.data)
    # 유효성 검사 후 통과 못하면 오류 반환
    if serializer.is_valid(raise_exception=True):
        # 유효성 검사 통과 시 저장 및 JSON 데이터 반환
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, article_pk):
    # 요청 pk와 같은 pk를 가진 인스턴스를 Article에서 찾아서 article 변수 저장
    # 없으면 오류를 반환
    article = get_object_or_404(Article, pk=article_pk)
    # 해당 article 삭제
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def detail(request, article_pk):
    # 요청 pk와 pk가 같은 인스턴스를 Article에서 찾아 변수에 저장
    article = get_object_or_404(Article, pk=article_pk)
    # article 정보 직렬화 후 데이터 반환
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
def cmtcreate(request, article_pk):
    # pk 일치하는 article 인스턴스 찾아 변수 저장
    article = get_object_or_404(Article, pk=article_pk)
    # 요청 데이터를 담아 comment 직렬화, article 정보 함께 넘겨주기
    serializer = CommentSerializer(data=request.data)
    # 유효성 검사 및 처리
    if serializer.is_valid(raise_exception=True):
        # article 필드에는 article 변수 정보 저장
        serializer.save(article=article)
        return Response(serializer.data)
    
@api_view(['PUT'])
def cmtupdate(request, article_pk, comment_pk):
    # 요청과 pk 일치하는 article, comment 인스턴스 찾아 변수 저장
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 해당 comment에 요청 정보를 담아 직렬화
    serializer = CommentSerializer(comment, data=request.data)
    # 유효성 검사 후 처리
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data)
    
@api_view(['DELETE'])
def cmtdelete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)