# Generated by Django 4.2.3 on 2023-08-04 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advertisements',
            new_name='Advertisement',
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]
