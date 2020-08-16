import os
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


def path_and_rename(instance, filename):
    upload_to = 'users/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class Profile(models.Model):
    # STYLE_CHOICES = (
    #     ("1", "1"),
    #     ("2", "2"),
    #     ("3", "3"),
    #     ("4", "4"),
    #     ("5", "5"),
    #     ("6", "6"),
    #     ("7", "7"),
    #     ("8", "8"),
    # )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to=path_and_rename, blank=True, null=True, default="profilePic.png")
    # avatar = models.ImageField(upload_to='users/', blank=True, null=True, default="profilePic.png")
    is_pro = models.BooleanField(default=False)
    bio = models.TextField(max_length=1000)
    # profile_style = models.CharField(max_length=100, choices=STYLE_CHOICES)

    instagram_url = models.URLField(max_length=255, blank=True, null=True)
    youtube_url = models.URLField(max_length=255, blank=True, null=True)
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    twitter_url = models.URLField(max_length=255, blank=True, null=True)

    # TODO Profile Styles
    # bg_class = models.CharField(max_length=100, null=True, blank=True)
    # border_class = models.CharField(max_length=100, null=True, blank=True)

    # profile_viewed_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Profile for user {self.user.username}'
