# Generated by Django 5.1.1 on 2024-09-29 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='data_opened',
            new_name='date_opened',
        ),
    ]
