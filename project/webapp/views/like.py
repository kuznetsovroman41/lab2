from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from ..models import Post, Like

class LikePostView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        return HttpResponseRedirect(reverse('post_detail', kwargs={'pk': pk}))
