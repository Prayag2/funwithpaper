# Generated by Django 3.0.6 on 2020-05-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fwp', '0004_auto_20200522_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='image',
        ),
        migrations.AddField(
            model_name='game',
            name='image_link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]