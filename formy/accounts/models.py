from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    followers = models.ManyToManyField('self', symmetrical=False, related_name="followed_by", blank=True, null=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True, null=True)

    def __str__(self):
        return self.username
