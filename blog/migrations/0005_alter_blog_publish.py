# Generated by Django 5.0.7 on 2024-07-19 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 17, 30, 19, 461646)),
        ),
    ]
