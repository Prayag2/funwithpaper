# Generated by Django 3.0.6 on 2021-05-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fwp', '0015_auto_20210505_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='pub_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]