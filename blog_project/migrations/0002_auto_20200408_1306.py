# Generated by Django 3.0.4 on 2020-04-08 07:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 7, 6, 25, 322910, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_dete',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 7, 6, 25, 319918, tzinfo=utc)),
        ),
    ]
