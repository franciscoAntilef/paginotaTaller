# Generated by Django 2.0.4 on 2018-05-03 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180426_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu',
            name='socket',
        ),
    ]
