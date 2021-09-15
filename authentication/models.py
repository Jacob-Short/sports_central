from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone


class SportsUser(AbstractUser):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    friend = models.ManyToManyField('self', symmetrical=False, blank=True)
    account_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name