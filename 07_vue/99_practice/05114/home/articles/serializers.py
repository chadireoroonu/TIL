from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    # 어떤 article에 달릴 댓글인지 정보
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    # comments를 추가한 정보 직렬화
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'