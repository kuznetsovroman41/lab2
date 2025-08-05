from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from ..models import Post, Comment

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        text = request.POST.get('text')
        if text:
            Comment.objects.create(author=request.user, post=post, text=text)
        return redirect('webapp:post_detail', pk=pk)
