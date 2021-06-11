from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, EditUpdateView, DeleteArticleView, ArticleCategoryView, ArticleCommentView


app_name = 'articles'

urlpatterns = [
    #path('', views.article_list, name="list"),
    #path('article/<int:pk>', views. article_detail, name="detail"),
    #path('create/', views.article_create, name="create"),
    path('', ArticleListView.as_view(), name="list"),
    path('article/<int:pk>',ArticleDetailView.as_view(), name="detail"),
    path('create/',ArticleCreateView.as_view(), name="create"),
    path('add_category/',ArticleCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>',EditUpdateView.as_view(), name="edit"),  
    path('article/<int:pk>/remove',DeleteArticleView.as_view(), name="delete"),
    path('category/<str:cats>/',views.CategoryView, name="category"),
    path('category-list/',views.CategoryListView, name="category-list"),
    path('like/<int:pk>', views.LikeView, name="like_article"),
    path('article/<int:pk>/comment/',ArticleCommentView.as_view(),name='add_comment')
]

