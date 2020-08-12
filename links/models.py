import os
from uuid import uuid4

# from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


def path_and_rename(instance, filename):
    upload_to = 'links/%Y/%m/%d/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Link(models.Model):
    order = models.IntegerField
    title = models.CharField(max_length=255)
    # link_id = models.CharField(max_length=255) #User_id + self.id
    url = models.URLField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links')
    # image = models.ImageField(upload_to='links/%Y/%m/%d/')
    image = models.ImageField(upload_to=path_and_rename)
    description = models.TextField(max_length=1000, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    num_clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
