# Generated by Django 4.0.3 on 2022-04-13 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tellmeastory', '0005_alter_node_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='image',
            field=models.ImageField(upload_to='storyimages'),
        ),
    ]