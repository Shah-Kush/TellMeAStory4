# Generated by Django 4.0.3 on 2022-04-13 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tellmeastory', '0009_node_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='image',
            field=models.ImageField(default=None, upload_to='media/storyimages'),
        ),
    ]