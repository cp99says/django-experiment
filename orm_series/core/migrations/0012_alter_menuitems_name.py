# Generated by Django 5.1.1 on 2024-11-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_menuitems_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
