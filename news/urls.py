from django.urls import path

from . import views


urlpatterns = [
   path('', views.PostList.as_view(), name='post_list'),
   path('search', views.PostSearchList.as_view(), name='post_search_list'),
   # pk — это первичный ключ поста, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),

   path('news/create/', views.NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/edit/', views.NewsUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', views.NewsDelete.as_view(), name='news_delete'),

   path('articles/create/', views.ArticlesCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit/', views.ArticlesUpdate.as_view(), name='articles_update'),
   path('articles/<int:pk>/delete/', views.ArticlesDelete.as_view(), name='articles_delete'),
]