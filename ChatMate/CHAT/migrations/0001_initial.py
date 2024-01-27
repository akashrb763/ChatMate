# Generated by Django 5.0.1 on 2024-01-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=18)),
                ('l_name', models.CharField(max_length=18)),
                ('birthdate', models.DateField()),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=18)),
                ('l_name', models.CharField(max_length=18)),
                ('birthdate', models.DateField()),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=12)),
                ('u_name', models.CharField(max_length=25)),
                ('link', models.CharField(max_length=50)),
            ],
        ),
    ]