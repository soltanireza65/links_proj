from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    STYLE_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    is_pro = models.BooleanField(default=False)
    bio = models.TextField(max_length=1000)
    profile_style = models.CharField(max_length=100, choices=STYLE_CHOICES)

    # TODO Profile Styles
    # bg_class = models.CharField(max_length=100, null=True, blank=True)
    # border_class = models.CharField(max_length=100, null=True, blank=True)

    # profile_viewed_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Profile for user {self.user.username}'
