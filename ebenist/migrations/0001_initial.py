# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-15 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categ', models.CharField(default=b'none', max_length=10, verbose_name='Nom categorie')),
            ],
            options={
                'db_table': 'categorie',
                'verbose_name': 'categorie',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Meuble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(default=b'-', max_length=40, verbose_name='Titre')),
                ('description', models.TextField(blank=True, default=b'-', null=True, verbose_name='Description')),
                ('fk_categ', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fk_categ', to='ebenist.Categorie', verbose_name='Categorie')),
            ],
            options={
                'db_table': 'meuble',
                'verbose_name': 'meuble',
                'verbose_name_plural': 'meubles',
            },
        ),
    ]
