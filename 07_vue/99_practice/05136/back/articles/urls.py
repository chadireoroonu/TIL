from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('create/', views.create),
    path('update/<int:article_pk>/', views.update),
    path('delete/<int:article_pk>/', views.delete),
    path('<int:article_pk>/', views.detail),
    path('<int:article_pk>/create/', views.cmtcreate),
    path('<int:article_pk>/<int:comment_pk>/update/', views.cmtupdate),
    path('<int:article_pk>/<int:comment_pk>/delete/', views.cmtdelete),
]
