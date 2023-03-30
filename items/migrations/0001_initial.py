# Generated by Django 4.1.7 on 2023-03-13 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='default.png', upload_to='item_images')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_price', models.DecimalField(decimal_places=1, max_digits=10000000000)),
                ('add_material', models.CharField(max_length=50)),
                ('add_main_category', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Kids', 'Kids')], default=None, max_length=50)),
                ('add_subcategory', models.CharField(choices=[('Clothing', 'Clothing'), ('Shoes', 'Shoes'), ('Bags', 'Bags'), ('Accessories', 'Accessories')], default=None, max_length=50)),
                ('add_description', models.TextField(default=None, max_length=1000)),
                ('add_color', models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Green', 'Green'), ('Blue', 'Blue')], default=None, max_length=50)),
                ('add_shoes_size', models.CharField(choices=[('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40')], default=None, max_length=50)),
                ('add_clothing_size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L')], default=None, max_length=50)),
                ('add_image', models.ManyToManyField(to='items.image')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]