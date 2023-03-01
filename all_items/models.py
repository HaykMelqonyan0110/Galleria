from django.db import models


class MainCategory(models.Model):
    main_category = models.CharField("name", max_length=50)

    def __str__(self):
        return self.main_category


class SubCategory(models.Model):
    sub_category = models.CharField("name", max_length=50)

    def __str__(self):
        return self.sub_category


class ClothingSize(models.Model):
    clothing_size = models.CharField("size", max_length=50)

    def __str__(self):
        return self.clothing_size


class ShoesSize(models.Model):
    shoes_size = models.CharField("size", max_length=40)

    def __str__(self):
        return self.shoes_size


class Colors(models.Model):
    colors = models.CharField('color', max_length=50)

    def __str__(self):
        return self.colors


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    cloth_size = models.ForeignKey(ClothingSize, on_delete=models.CASCADE, default=None)
    sh_size = models.ForeignKey(ShoesSize, on_delete=models.CASCADE, default=None)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.name}, {self.category}, {self.subcategory}'

