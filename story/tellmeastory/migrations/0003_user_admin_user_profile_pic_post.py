# Generated by Django 4.0.3 on 2022-04-27 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tellmeastory', '0002_remove_report_id_alter_report_reporting_username')#'0002_user_mature'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.CharField(default='', max_length=72, primary_key=True, serialize=False)),
                ('postText', models.CharField(default='', max_length=200)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tellmeastory.user')),
            ],
        ),
    ]
