# Generated by Django 2.2.1 on 2019-06-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcoursup', '0005_auto_20190528_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('insee', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=200)),
            ],
        ),
    ]