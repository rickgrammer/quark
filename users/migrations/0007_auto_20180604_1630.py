# Generated by Django 2.0.5 on 2018-06-04 11:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180527_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^\\+?\\d{10,12}$')]),
        ),
    ]