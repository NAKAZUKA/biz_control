# Generated by Django 4.2.13 on 2024-05-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_space', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='address',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
