# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcoursup', '0006_auto_20180522_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='proposition_actuelle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='parcoursup.Proposition'),
        ),
    ]
