# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcoursup', '0011_classe_groupe_parcoursup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='date_naissance',
            field=models.DateField(blank=True, null=True, verbose_name='date de naissance'),
        ),
    ]
