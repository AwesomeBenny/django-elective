from django.db import models
from django.contrib.auth.models import User


class TodoItem(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    status = models.BooleanField()
