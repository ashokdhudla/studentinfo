# Generated by Django 3.0.1 on 2020-02-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.IntegerField(blank=True, null=True)),
                ('second', models.IntegerField(blank=True, null=True)),
                ('third', models.IntegerField(blank=True, null=True)),
                ('fourth', models.IntegerField(blank=True, null=True)),
                ('fifth', models.IntegerField(blank=True, null=True)),
                ('sixth', models.IntegerField(blank=True, null=True)),
                ('seventh', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
