from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Completed = models.BooleanField(default=False)

