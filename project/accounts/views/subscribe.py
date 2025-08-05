from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from accounts.models import Subscription

User = get_user_model()

class SubscribeToggleView(LoginRequiredMixin, View):

    def post(self, request, username, *args, **kwargs):
        user_to_subscribe = get_object_or_404(User, username=username)
        if user_to_subscribe == request.user:
            return redirect('accounts:user_profile', username=username)

        subscription = Subscription.objects.filter(
            follower=request.user,
            following=user_to_subscribe
        ).first()

        if subscription:
            subscription.delete()
        else:
            Subscription.objects.create(follower=request.user, following=user_to_subscribe)

        return redirect('accounts:user_profile', username=username)
