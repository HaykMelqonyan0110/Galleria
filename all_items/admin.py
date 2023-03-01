from django.contrib import admin
from .models import MainCategory, SubCategory, ShoesSize, ClothingSize, Colors, Product

admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(ShoesSize)
admin.site.register(ClothingSize)
admin.site.register(Colors)
admin.site.register(Product)


