# Generated by Django 4.2.4 on 2023-08-07 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0004_curso_turno'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='profesion',
            field=models.CharField(default='profesor', max_length=50),
        ),
    ]