from django.urls import path
from . import views

# app_name은 반드시 이 변수명으로 작성해야 정상 작동
app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create')
]
