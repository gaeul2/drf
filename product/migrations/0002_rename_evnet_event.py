# Generated by Django 4.0.5 on 2022-06-20 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Evnet',
            new_name='Event',
        ),
    ]