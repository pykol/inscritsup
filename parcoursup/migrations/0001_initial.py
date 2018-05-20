# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.SmallIntegerField(choices=[(0, "Envoi du dossier d'inscription"), (1, "Envoi du dossier pour l'internat"), (2, 'Inscription administrative'), (3, 'Demande de pi\xe8ces compl\xe9mentaires'), (4, "Enregistrement d'une d\xe9mission")], verbose_name='cat\xe9gorie')),
                ('date', models.DateTimeField()),
                ('date_fait', models.DateTimeField(blank=True, null=True)),
                ('statut', models.SmallIntegerField(choices=[(0, '\xc0 traiter'), (1, 'Fait'), (2, 'Rien \xe0 faire')])),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100, verbose_name='pr\xe9nom')),
                ('date_naissance', models.DateField(verbose_name='date de naissance')),
                ('email', models.EmailField(max_length=254)),
                ('dossier_parcoursup', models.IntegerField(primary_key=True, serialize=False, verbose_name='num\xe9ro de dossier')),
            ],
        ),
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_proposition', models.DateTimeField()),
                ('date_demission', models.DateTimeField(blank=True, null=True)),
                ('internat', models.BooleanField()),
                ('statut', models.SmallIntegerField(choices=[(0, 'Oui d\xe9finitif'), (1, 'Autres v\u0153ux en attente')])),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcoursup.Classe')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcoursup.Etudiant')),
                ('remplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parcoursup.Proposition')),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='proposition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcoursup.Proposition'),
        ),
    ]