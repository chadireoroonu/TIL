from django.db import models

# 모델명은 첫 글자 대문자, 단수형
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    # 댓글을 남길 article 정보 정참조
    # Article 모델의 pk키 참조, 참조 중인 article 삭제 시 함께 삭제
    # Article 모델에서 역참조 시 부를 이름은 comments
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()