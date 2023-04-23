# project > urls.py
- path('api/v1/', include(app.urls)),
- 이제 앱이름 대신 api/v1 사용

# rest framework
1. pip install djangorestframework
2. settings.py > INSTALLED_APP > 'rest_framework', 추가
3. views.py > import
```
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
```

# manytomanyfield
- movie_actors 이름으로 만들고 싶을 때
1. models.py > Movie
```
actors = models.ManyToManyField(Actor, related_name='movies')
```
2. related_name : 역참조시 사용할 이름

# serializers
1. app > serializers.py 파일 생성
2. rest_framework, Model import
```
from rest_framework import serializers
from .models import Movie, Actor, Review
```