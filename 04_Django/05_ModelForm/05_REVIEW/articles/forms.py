from django import forms
from .models import Article
# 다른 이름의 파일로 만들어도 상관 없음

# Model에 대한 정보를 바탕으로 Form 생성할 수 있는 class
class ArticleForm(forms.ModelForm):
    
    class Meta:
        # 내가 정의한 class Article을 토대로 Form 생성
        model = Article
        # Article 클래스에는 field 들이 정의되어 있음
        # field -> table의 각 column을 정의한 것
        # database에 만들어진 table에 저장한 값들
        # 내 article table에 저장해야 하는 값들을 모두 form으로 만들기
        fields = '__all__'