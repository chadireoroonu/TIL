from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    # Article 모델의 모든 인스턴스 article 변수에 담기
    article = Article.objects.all()
    # article 내용을 ArticleSerializer로 직렬화, 여러 개
    serializer = ArticleSerializer(article, many=True)
    # serializer의 데이터 반환
    return Response(serializer.data)