# Generated by Django 3.2.7 on 2024-07-31 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(max_length=16),
        ),
    ]
