from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..forms.post import PostCreateForm
from ..models import Post, Like
from django.views.generic.detail import DetailView

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'webapp/post_create.html'
    success_url = reverse_lazy('webapp:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['has_liked'] = Like.objects.filter(user=self.request.user, post=self.object).exists()
        return context
