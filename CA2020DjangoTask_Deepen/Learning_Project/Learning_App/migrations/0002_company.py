# Generated by Django 2.1 on 2020-08-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learning_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=10)),
                ('phone', models.IntegerField(default=0)),
                ('add', models.CharField(max_length=20)),
            ],
        ),
    ]
