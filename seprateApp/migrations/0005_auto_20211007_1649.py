# Generated by Django 3.2.7 on 2021-10-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seprateApp', '0004_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]