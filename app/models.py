from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    choose = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


