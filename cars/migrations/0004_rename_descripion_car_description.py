# Generated by Django 5.0.6 on 2024-05-31 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_is_displayed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='descripion',
            new_name='description',
        ),
    ]
