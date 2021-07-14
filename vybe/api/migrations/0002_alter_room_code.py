# Generated by Django 3.2.5 on 2021-07-14 12:37

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.generateUniqueCode, max_length=8, unique=True),
        ),
    ]
