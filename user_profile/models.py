from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms


GENDER_CHOICES = (
    ("Male", 'Male'),
    ("Female", 'Female'),
    ("-", "-")
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.png', upload_to='profile_pics')
    first_name = models.CharField(max_length=50, default="First name")
    last_name = models.CharField(max_length=50, default="Last Name")
    gender_fields = models.CharField(max_length=50, choices=GENDER_CHOICES, default="-")

    def __str__(self):
        return f'{self.user.username}s profile'

    def get_absolute_url(self):
        return reverse('account')






