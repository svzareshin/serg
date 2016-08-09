from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class BlogArtical(models.Model):

    author = models.ForeignKey(User)
    title =  models.CharField(max_length=256)
    context = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    changer = models.DateTimeField(auto_now=True)