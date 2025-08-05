from django.urls import path
from .views.post import PostCreateView
from .views.home import HomeFeedView

app_name = 'webapp'

urlpatterns = [
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('', HomeFeedView.as_view(), name='home_feed'),
]






