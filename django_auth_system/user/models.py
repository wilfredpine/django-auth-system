from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)  # Ensures unique email

    def __str__(self):
        return self.username
