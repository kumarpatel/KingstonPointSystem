from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone


class Point(models.Model):
    # author = models.ForeignKey('auth.User')
    # title = models.CharField(max_length=200)
    points = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.points
