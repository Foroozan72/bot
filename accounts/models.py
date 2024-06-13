from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)  # Adjust max length as needed
    otp = models.CharField(max_length=6, null=True, blank=True)  # For OTP verification
    
    # Add unique related_name attributes to prevent reverse accessor clashes
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Unique related_name for groups
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Unique related_name for permissions
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )

    def __str__(self):
        return self.username

