# Generated by Django 4.0.3 on 2022-04-13 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tellmeastory', '0007_alter_node_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='image',
        ),
    ]