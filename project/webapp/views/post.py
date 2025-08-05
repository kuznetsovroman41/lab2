from django.urls import reverse_lazy
from django.views.generic import CreateView
from webapp.forms.post import PostCreateForm
from webapp.models.post import Post

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'webapp/post_create.html'
    success_url = reverse_lazy('webapp:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response
