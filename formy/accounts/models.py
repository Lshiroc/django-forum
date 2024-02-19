from django.contrib.auth.models import AbstractUser
from django.db import models

from post.models import Post

class CustomUser(AbstractUser):
    pass
    followers = models.ManyToManyField('self', symmetrical=False, related_name="followed_by")
    following = models.ManyToManyField('self', symmetrical=False)
    posts = models.ManyToManyField(Post, symmetrical=False)
    profile_picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.username
