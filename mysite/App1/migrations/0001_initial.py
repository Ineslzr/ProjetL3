# Generated by Django 3.2.7 on 2021-11-26 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('prenom', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telephone', models.CharField(blank=True, max_length=10, null=True)),
                ('code_postal', models.CharField(blank=True, max_length=255, null=True)),
                ('ville', models.CharField(blank=True, max_length=255, null=True)),
                ('adresse', models.CharField(blank=True, max_length=255, null=True)),
                ('nb_parts', models.CharField(blank=True, max_length=10, null=True)),
                ('mot_mairie', models.CharField(blank=True, max_length=10, null=True)),
                ('carte_donne', models.CharField(blank=True, max_length=10, null=True)),
                ('remarque', models.TextField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'beneficiaire',
            },
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_beneficiaire', models.IntegerField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'presence',
            },
        ),
    ]
