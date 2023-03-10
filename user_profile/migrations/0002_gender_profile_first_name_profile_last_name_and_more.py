# Generated by Django 4.1.7 on 2023-03-11 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genders', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='First name', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Last Name', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user_profile.gender'),
        ),
    ]
