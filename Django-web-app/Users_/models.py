from django.db import models
from django.contrib.auth.models import User

"""
models.py

Defines the Profile model, which extends user information beyond Django's built-in authentication system.

Each Profile instance is linked to a corresponding User instance via a one-to-one relationship.
"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


def __str__(self):    
    return f'{self.user.username} Profile'