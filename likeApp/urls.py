from django.urls import path

from likeApp.views import *

app_name = 'likeApp'

urlpatterns = [
    path('article/<int:article_pk>', LikeArticleView.as_view(), name='article_like'),
]