from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('create/', views.create),
    path('update/<int:article_pk>/', views.update),
    path('delete/<int:article_pk>/', views.delete),
]