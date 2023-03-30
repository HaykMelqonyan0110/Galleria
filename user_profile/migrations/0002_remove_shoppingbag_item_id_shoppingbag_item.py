# Generated by Django 4.1.7 on 2023-03-24 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_item_add_image_alter_item_add_clothing_size_and_more'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingbag',
            name='item_id',
        ),
        migrations.AddField(
            model_name='shoppingbag',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.item'),
        ),
    ]