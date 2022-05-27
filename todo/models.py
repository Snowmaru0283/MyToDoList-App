from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name='todos', default=None)
    title = models.CharField(max_length=100)
    Completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'