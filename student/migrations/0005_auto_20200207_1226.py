# Generated by Django 3.0.1 on 2020-02-07 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200207_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Subject'),
        ),
    ]
