from django.urls import path
from .views.post import PostCreateView
from .views.home import HomeFeedView
from .views.like import LikePostView
from .views.post_detail import PostDetailView


app_name = 'webapp'

urlpatterns = [
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('', HomeFeedView.as_view(), name='home_feed'),
    path('post/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]






