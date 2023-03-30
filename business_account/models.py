from django.db import models
from django.contrib.auth.models import User
from items.models import Item
from user_profile.models import ShoppingBag


class BusinessAccount(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, default="Company Name")
    company_email = models.EmailField(default="Company Email")
    company_phone = models.IntegerField()
    company_image = models.ImageField(default="default.png", upload_to='company_images')

    def __str__(self):
        return self.company_name


class BusinessAccountOrders(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer')
    buyer_item = models.CharField(max_length=500)
    owner_item = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_item')
