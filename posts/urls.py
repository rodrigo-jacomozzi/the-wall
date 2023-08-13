from django.urls import path

from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post'),
]
