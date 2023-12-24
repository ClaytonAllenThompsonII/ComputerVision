from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User  # For the User model
from .models import Profile  # For the Profile model

# Handles signals to automate the creation and updating of Profile instances in conjunction with User instances.
# Listens for the 'post_save' signal sent when a User is saved. If a new User is created, a corresponding Profile is also created.
# If an existing User is updated, their associated Profile is saved as well, ensuring consistency between the two models.


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance,created, **kwargs):
    instance.profile.save()