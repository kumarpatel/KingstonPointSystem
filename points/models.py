from __future__ import unicode_literals

from django.db import models


class Alias(models.Model):
    text = models.CharField(max_length=255, blank=False)
    created_by = models.ForeignKey("auth.User", related_name="alias", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.text


class Point(models.Model):
    amount = models.IntegerField()
    person = models.ForeignKey("auth.User", related_name="points")
    assigned_by = models.ForeignKey("auth.User", related_name="assigned_by")

    alias = models.ForeignKey(Alias, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.amount)


#
# class Comment(models.Model):
#     text = models.CharField(max_length=255, blank=False)
#     created_by = models.ForeignKey("auth.User", related_name="created_by")
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ('created',)
#
#     def __str__(self):
#         return self.text
