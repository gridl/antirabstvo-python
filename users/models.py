from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.TextField(max_length = 12)
    is_employer = models.BooleanField(default=False)
        