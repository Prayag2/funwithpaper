# Generated by Django 3.0.6 on 2020-05-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fwp', '0003_auto_20200522_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='image_link',
        ),
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]