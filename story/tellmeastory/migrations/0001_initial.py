# Generated by Django 4.0.3 on 2022-04-14 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('managetags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=512)),
                ('display_name', models.CharField(max_length=200)),
                ('user_blurb', models.CharField(max_length=1000, default="")),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='storyimages')),
                ('image_url', models.TextField()),
                ('node_title', models.CharField(max_length=200)),
                ('node_content', models.CharField(max_length=10000)),
                ('has_image_file', models.BooleanField(default=False)),
                ('node_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tellmeastory.user')),
                ('other_tags', models.ManyToManyField(to='managetags.tag')),
            ],
        ),
    ]