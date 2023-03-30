from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import reverse


MAIN_CHOICES = (
    ('select', "Select"),
    ("men", "Men"),
    ("women", "Women"),
    ("kids", "Kids")
)

SUB_CHOICES = (
    ('select', "Select"),
    ("clothing", "Clothing"),
    ("shoes", "Shoes"),
    ("bags", "Bags"),
    ("accessories", "Accessories")
)


COLOR_CHOICES = (
    ('select', "Select"),
    ("black", "Black"),
    ("white", "White"),
    ("red", "Red"),
    ("green", "Green"),
    ("blue", "Blue")
)

SHOES_SIZE_CHOICES = (
    ('select', "Select"),
    ("35", "35"),
    ("36", "36"),
    ("37", "37"),
    ("38", "38"),
    ("39", "39"),
    ("40", "40")
)


CLOTHING_SIZE_CHOICES = (
    ('select', "Select"),
    ("s", "S"),
    ("m", "M"),
    ("l", "L")
)


class Item(LoginRequiredMixin, UserPassesTestMixin, models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    add_name = models.CharField(max_length=200, default=None)
    add_price = models.DecimalField(max_digits=10000000000, decimal_places=1)
    add_material = models.CharField(max_length=50)
    add_main_category = models.CharField(max_length=50, choices=MAIN_CHOICES, default=None)
    add_subcategory = models.CharField(max_length=50, choices=SUB_CHOICES, default=None)
    add_description = models.TextField(max_length=1000, default=None)
    add_color = models.CharField(max_length=50, choices=COLOR_CHOICES, default=None)
    add_shoes_size = models.CharField(max_length=50, choices=SHOES_SIZE_CHOICES, default=None)
    add_clothing_size = models.CharField(max_length=50, choices=CLOTHING_SIZE_CHOICES, default=None)
    add_image = models.ImageField(default='default.img', upload_to='item_images')

    def __str__(self):
        return self.add_name


    def get_absolute_url(self):
        return reverse('bs_account_details')

