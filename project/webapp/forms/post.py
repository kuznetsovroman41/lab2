from django import forms
from ..models.post import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']
