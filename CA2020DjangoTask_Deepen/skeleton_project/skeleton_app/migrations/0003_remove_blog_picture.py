# Generated by Django 3.0.3 on 2020-09-01 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton_app', '0002_auto_20200901_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='picture',
        ),
    ]