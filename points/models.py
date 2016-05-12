from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone


class Point(models.Model):
    assigned_by = models.ForeignKey("auth.User")
    assigned_to = models.ForeignKey("auth.User")
    comment = models.CharField(max_length=200, blank=False)
    alias = models.CharField(blank=True)
    points = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.points
