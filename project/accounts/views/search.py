from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.db.models import Q
from ..forms import UserSearchForm

User = get_user_model()

class UserSearchView(ListView):
    model = User
    template_name = 'accounts/user_search.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        form = UserSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query:
                return User.objects.filter(
                    Q(username__icontains=query) |
                    Q(email__icontains=query) |
                    Q(first_name__icontains=query)
                )
        return User.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserSearchForm(self.request.GET)
        return context
