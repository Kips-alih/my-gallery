# Generated by Django 3.2 on 2021-11-27 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20211127_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]
