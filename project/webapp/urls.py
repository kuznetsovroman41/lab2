from django.urls import path
from webapp.views.post import PostCreateView

app_name = 'webapp'

urlpatterns = [
    path('posts/create/', PostCreateView.as_view(), name='post_create'),

]






