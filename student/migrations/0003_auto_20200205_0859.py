# Generated by Django 3.0.1 on 2020-02-05 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200118_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addmarks',
            name='dateofexam',
        ),
        migrations.RemoveField(
            model_name='addmarks',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='addmarks',
            name='lastname',
        ),
    ]
