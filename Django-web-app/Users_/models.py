from django.db import models
from django.contrib.auth.models import User



# Defines the Profile model, which extends user information beyond Django's built-in authentication system.
# Each Profile instance is linked to a corresponding User instance via a one-to-one relationship.


class Profile(models.Model):
    """Represents extended user information beyond the default User model.

    Stores additional profile-specific data associated with a particular user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a human-readable representation of the Profile instance.

        Used for display purposes in the Django admin and other parts of the application.
        """   
        return f'{self.user.username} Profile'
    
