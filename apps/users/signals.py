from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ProfileUser

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileUser(user=instance, email=instance.email).save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User)
def update_profile_email(sender, instance, **kwargs):
    """ Make sure profile.email same as user.email """
    if hasattr(instance, 'email'): # make sure user have email
        instance.profile.email = instance.email
        instance.profile.save()