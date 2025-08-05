from django.db import models
from django.conf import settings
from django import forms

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Публикация {self.id} от {self.author.username}'


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']


