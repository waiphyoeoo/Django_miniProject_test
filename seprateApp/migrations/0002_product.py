# Generated by Django 3.2.7 on 2021-09-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seprateApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productsName', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
