from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'add_name',
            'add_price',
            'add_material',
            'add_main_category',
            'add_subcategory',
            'add_description',
            'add_color',
            'add_shoes_size',
            'add_clothing_size',
            "add_image",
        ]



