# Generated by Django 4.0.4 on 2022-04-14 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tellmeastory', '0012_alter_report_report_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='report_id',
        ),
        migrations.AddField(
            model_name='report',
            name='id_for_report',
            field=models.CharField(default='', max_length=100),
        ),
    ]