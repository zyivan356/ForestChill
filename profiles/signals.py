from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Relationship

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    # print('sender', sender)
    # print('instance', instance)
    if created:
        Profile.objects.create(user=instance)


# Add friend
@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender = instance.sender
    receiver = instance.receiver
    if instance.status == 'accepted':
        sender.friends.add(receiver.user)
        receiver.friends.add(sender.user)
        sender.save()
        receiver.save()


# Delete from friends
@receiver(pre_delete, sender=Relationship)
def pre_delete_remove_friends(sender, instance, **kwargs):
    sender = instance.sender
    receiver = instance.receiver
    sender.friends.remove(receiver.user)
    receiver.friends.remove(sender.user)
    sender.save()
    receiver.save()