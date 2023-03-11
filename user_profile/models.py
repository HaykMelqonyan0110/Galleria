from django.db import models
from django.contrib.auth.models import User


class Gender(models.Model):
    genders = models.CharField(max_length=50, null=True, blank=True, default=None)

    def __str__(self):
        return self.genders


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.png', upload_to='profile_pics')
    first_name = models.CharField(max_length=50, default="First name")
    last_name = models.CharField(max_length=50, default="Last Name")
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.user.username}s profile'






