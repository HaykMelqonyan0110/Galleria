from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from items.models import Item


GENDER_CHOICES = (
    ('select', "Select"),
    ("Male", 'Male'),
    ("Female", 'Female'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default="First name")
    last_name = models.CharField(max_length=50, default="Last Name")
    gender_fields = models.CharField(max_length=50, choices=GENDER_CHOICES, default="-")
    phone_number = models.IntegerField(default=374)
    address = models.CharField(max_length=100, default='Your address')

    def __str__(self):
        return f'{self.user.username}s profile'

    def get_absolute_url(self):
        return reverse('account')


class ShoppingBag(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=1)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

