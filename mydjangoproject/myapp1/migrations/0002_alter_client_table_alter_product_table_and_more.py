# Generated by Django 4.1 on 2024-11-15 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='client',
            table='Clients',
        ),
        migrations.AlterModelTable(
            name='product',
            table='Product',
        ),
        migrations.AlterModelTable(
            name='sale',
            table='Sales',
        ),
    ]
