from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import get_object_or_404
from ..models import Post, Like

class LikePostView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        like_obj = Like.objects.filter(user=request.user, post=post)
        if like_obj.exists():
            like_obj.delete()
        else:
            Like.objects.create(user=request.user, post=post)  # поставить лайк
        return HttpResponseRedirect(reverse('webapp:post_detail', kwargs={'pk': pk}))
