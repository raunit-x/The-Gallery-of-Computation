# Generated by Django 3.1.2 on 2020-11-01 18:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_merge_20201031_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='expiry_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2020, 11, 2, 18, 11, 13, 316467, tzinfo=utc)),
        ),
    ]