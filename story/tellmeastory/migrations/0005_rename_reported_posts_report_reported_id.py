# Generated by Django 4.0.4 on 2022-04-12 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tellmeastory', '0004_rename_reported_username_report_reported_posts_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='reported_posts',
            new_name='reported_id',
        ),
    ]
