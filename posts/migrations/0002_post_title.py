# Generated by Django 4.2.2 on 2023-07-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='null', max_length=1000),
        ),
    ]