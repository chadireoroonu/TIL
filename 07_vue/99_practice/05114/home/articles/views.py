from rest_framework.decorators import api_view
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def index(request):
    # 모든 article 인스턴스 가져오기
    article = Article.objects.all()
    # 가져온 인스턴스들 직렬화하기
    serializer = ArticleSerializer(article, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    # serializer에 요청 데이터를 넣어 직렬화
    serializer = ArticleSerializer(data=request.data)
    # 유효성 검사 통과시 저장, 반환하고 실패 시 오류 반환
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['PUT'])
def update(request, article_pk):
    # 게시물 중에서 수정하기를 원하는 것과 pk가 같은 인스턴스 하나를 가져옴
    article = get_object_or_404(Article, pk=article_pk)
    # article의 변경 내용을 담아 직렬화
    serializer = ArticleSerializer(article, data=request.data)
    # 유효성 검사 통과 시 저장, 반환하고 실패 시 오류 반환
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['DELETE'])
def delete(request, article_pk):
    # 삭제하려는 pk와 pk가 같은 인스턴스를 찾아와서 삭제
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def detail(request, article_pk):
    # pk가 일치하는 인스턴스 하나 들고오기
    article = Article.objects.get(pk=article_pk)
    # comment를 포함한 정보 직렬화 및 반환
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
def createcomment(request, article_pk):
    # 댓글을 달 article과 pk가 일치하는 것을 찾아옴
    article = get_object_or_404(Article, pk=article_pk)
    # 댓글 데이터 직렬화
    serializer = CommentSerializer(data=request.data)
    # 유효성 검사 통과 시 article에 해당 댓글 저장
    if serializer.is_valid(raise_exception=True):
        # 어떤 article에 달린 댓글인지 추가
        serializer.save(article=article)
        return Response(serializer.data)
    
@api_view(['PUT'])
def updatecomment(request, article_pk, comment_pk):
    # comment가 달려있는 article pk가 일치하는 인스턴스 찾아 가져오기
    article = get_object_or_404(Article, pk=article_pk)
    # 수정하고자 하는 comment pk와 일치하는 인스턴스 찾아 가져오기
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 수정 내용을 담아 직렬화
    serializer = CommentSerializer(comment, data=request.data)
    # 유효성 검사 후 유효하다면 article의 comment로 저장, 반환
    # 유효하지 않으면 오류 반환
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data)
    
@api_view(['DELETE'])
def deletecomment(request, article_pk, comment_pk):
    # 해당 comment가 달려있는 article pk와 일치하는 인스턴스 찾기
    article = get_object_or_404(Article, pk=article_pk)
    # 해당 comment pk와 일치하는 인스턴스 찾기
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 찾은 comment 삭제 후 204 HTTP 상태 반환
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)