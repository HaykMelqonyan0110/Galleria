# Generated by Django 4.1.7 on 2023-03-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_account', '0002_alter_businessaccountorders_buyer_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessaccountorders',
            name='buyer_item',
            field=models.CharField(max_length=500),
        ),
    ]
