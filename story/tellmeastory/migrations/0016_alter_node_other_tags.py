# Generated by Django 4.0.4 on 2022-04-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managetags', '0001_initial'),
        ('tellmeastory', '0015_alter_report_post_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='other_tags',
            field=models.ManyToManyField(blank=True, to='managetags.tag'),
        ),
    ]
