# Generated by Django 3.2 on 2023-04-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_auto_20230404_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
