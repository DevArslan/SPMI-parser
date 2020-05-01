# Generated by Django 2.2.5 on 2020-02-22 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scopusData',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=255)),
                ('creator', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('journal', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('volume', models.CharField(max_length=255)),
                ('issue', models.CharField(max_length=255)),
                ('pages', models.CharField(max_length=255)),
                ('doi', models.CharField(max_length=255)),
            ],
        ),
    ]