# Generated by Django 5.1.4 on 2024-12-18 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profes',
            name='foto',
            field=models.ImageField(null=True, upload_to='app_profes'),
        ),
    ]