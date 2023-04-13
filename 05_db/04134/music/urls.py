from django.urls import path
from . import views

# html에서 url 생성이 쉽게 하는 역할 -> 지금은 필요X, name도 같은 이유
# app_name = 'music'

urlpatterns = [
    path('music/', views.music_list_create), # 모든 음악 정보 조회
    path('music/<int:music_pk>/', views.music_detail),
]
