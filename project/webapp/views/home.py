from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from webapp.models import Post

class HomeFeedView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'webapp/home_feed.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        following_ids = user.subscriptions.values_list('following_id', flat=True)
        return Post.objects.filter(author_id__in=following_ids).order_by('-created_at')
