# Generated by Django 2.2.5 on 2020-01-24 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('academicDegree', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
            ],
        ),
    ]
