# Generated by Django 4.2.4 on 2023-08-03 18:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('edad_de_matrimonio', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('fecha_de_nacimiento', models.DateField()),
                ('rol', models.CharField(choices=[('yo', 'Yo'), ('hijo', 'Hijo'), ('padre', 'Padre'), ('madre', 'Madre'), ('abuelo_paterno', 'Abuelo Paterno'), ('abuela_paterna', 'Abuela Paterna'), ('abuelo_materno', 'Abuelo Materno'), ('abuela_materna', 'Abuela Materna')], default='yo', max_length=15)),
                ('padres', models.ManyToManyField(blank=True, related_name='hijos', to='appcoder.familiar')),
            ],
        ),
    ]