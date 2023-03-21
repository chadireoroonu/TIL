from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # 이미지를 넣지 않아도 게시글이 생성될 수 있도록 하는 조건 두 가지
    # blank=True -> DB에는 '' 빈 문자열 저장 -> 유효성 검사 시 통과 -> 일반적으로 사용
    # null=True -> DB에 NULL 저장 -> 값이 없으므로 문자열 기반 필드에서 사용 피하기
    image = models.ImageField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'
