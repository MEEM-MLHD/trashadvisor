# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-04 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0004_auto_20161104_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_declarant', models.IntegerField(max_length=11)),
                ('conteneur_type', models.CharField(max_length=20)),
                ('conteneur_couleur', models.CharField(max_length=20)),
                ('dechet_type', models.CharField(max_length=32)),
                ('code_postal', models.IntegerField(max_length=5)),
                ('code_insee', models.CharField(max_length=32)),
                ('declaration_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dustbin',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dustbin/'),
        ),
        migrations.AlterField(
            model_name='waste',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='waste/'),
        ),
    ]
