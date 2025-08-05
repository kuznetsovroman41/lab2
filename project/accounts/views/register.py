from django.urls import reverse_lazy
from django.views.generic import FormView
from ..forms.register import RegisterForm
from django.contrib.auth import login

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

