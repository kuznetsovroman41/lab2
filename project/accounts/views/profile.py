from django.views.generic import DetailView
from webapp.models import Post
from accounts.models import CustomUser

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'accounts/user_profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(author=self.object).order_by('-created_at')
        context['posts'] = posts
        return context
