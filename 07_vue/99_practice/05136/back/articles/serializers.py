from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields는 리스트 형태로 작성 주의
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    # comments는 CommentSerializer에서 참조, 여러 개, 읽기 전용
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'