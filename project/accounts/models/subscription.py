from django.conf import settings
from django.db import models

class Subscription(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='subscriptions', on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='subscribers', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower} -> {self.following}'
