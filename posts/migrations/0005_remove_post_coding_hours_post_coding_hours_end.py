# Generated by Django 4.2.2 on 2023-07-06 18:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_coding_hours_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='coding_hours',
        ),
        migrations.AddField(
            model_name='post',
            name='coding_hours_end',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
