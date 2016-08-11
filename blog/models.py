from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class BlogArticle(models.Model):

    author = models.ForeignKey(User)
    title =  models.CharField(max_length=256)
    context = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    changer = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return  self.title