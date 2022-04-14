# Generated by Django 4.0.4 on 2022-04-14 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tellmeastory', '0010_report_report_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='id',
        ),
        migrations.AlterField(
            model_name='report',
            name='reporting_username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tellmeastory.user'),
        ),
    ]