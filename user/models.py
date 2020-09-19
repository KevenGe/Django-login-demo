from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class WebUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.IntegerField(null=True, default=0)
