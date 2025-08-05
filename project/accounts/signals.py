from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Subscription
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=Subscription)
def increment_counters_on_subscribe(sender, instance, created, **kwargs):
    if created:
        follower = instance.follower
        following = instance.following
        follower.following_count += 1
        following.followers_count += 1
        follower.save(update_fields=['following_count'])
        following.save(update_fields=['followers_count'])

@receiver(post_delete, sender=Subscription)
def decrement_counters_on_unsubscribe(sender, instance, **kwargs):
    follower = instance.follower
    following = instance.following
    if follower.following_count > 0:
        follower.following_count -= 1
    if following.followers_count > 0:
        following.followers_count -= 1
    follower.save(update_fields=['following_count'])
    following.save(update_fields=['followers_count'])
