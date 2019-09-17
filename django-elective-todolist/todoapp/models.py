from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    status = models.BooleanField()
