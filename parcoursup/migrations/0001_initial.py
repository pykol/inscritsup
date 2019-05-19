# Generated by Django 2.2.1 on 2019-05-19 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True)),
                ('code_parcoursup', models.SmallIntegerField()),
                ('groupe_parcoursup', models.SmallIntegerField()),
                ('capacite', models.SmallIntegerField(verbose_name='capacité')),
                ('surbooking', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100, verbose_name='prénom')),
                ('date_naissance', models.DateField(blank=True, null=True, verbose_name='date de naissance')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=20, verbose_name='téléphone')),
                ('telephone_mobile', models.CharField(blank=True, max_length=20, verbose_name='téléphone mobile')),
                ('dossier_parcoursup', models.IntegerField(primary_key=True, serialize=False, verbose_name='numéro de dossier')),
                ('adresse', models.TextField(blank=True)),
                ('sexe', models.SmallIntegerField(blank=True, choices=[(1, 'M.'), (2, 'Mme')], null=True)),
            ],
            options={
                'verbose_name': 'étudiant',
            },
        ),
        migrations.CreateModel(
            name='ParcoursupMessageEnvoyeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ParcoursupSynchro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateTimeField(verbose_name='début')),
                ('date_fin', models.DateTimeField(verbose_name='fin')),
                ('mode', models.SmallIntegerField(choices=[(1, 'Automatique'), (2, 'Manuelle')])),
                ('resultat', models.SmallIntegerField(blank=True, choices=[(1, 'Réussie'), (2, 'Échec')], null=True, verbose_name='résultat')),
            ],
        ),
        migrations.CreateModel(
            name='ParcoursupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_proposition', models.DateTimeField()),
                ('date_demission', models.DateTimeField(blank=True, null=True)),
                ('internat', models.BooleanField()),
                ('cesure', models.BooleanField(verbose_name='césure')),
                ('etat', models.SmallIntegerField(choices=[(0, 'Oui définitif'), (1, 'Autres vœux en attente')])),
                ('inscription', models.BooleanField(verbose_name='inscription réalisée')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcoursup.Classe')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcoursup.Etudiant')),
                ('remplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='remplacee_par', to='parcoursup.Proposition')),
            ],
            options={
                'get_latest_by': 'date_proposition',
            },
        ),
        migrations.CreateModel(
            name='ParcoursupMessageRecuLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('ip_source', models.GenericIPAddressField()),
                ('endpoint', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=200)),
                ('succes', models.BooleanField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parcoursup.ParcoursupUser')),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='proposition_actuelle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='parcoursup.Proposition'),
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.SmallIntegerField(choices=[(0, "Envoi du dossier d'inscription"), (1, "Envoi du dossier pour l'internat"), (2, 'Inscription administrative'), (3, 'Demande de pièces complémentaires'), (4, "Enregistrement d'une démission")], verbose_name='catégorie')),
                ('date', models.DateTimeField()),
                ('date_fait', models.DateTimeField(blank=True, null=True)),
                ('etat', models.SmallIntegerField(choices=[(0, 'À traiter'), (1, 'Fait'), (2, 'Rien à faire'), (3, 'Annulée')], default=0)),
                ('message', models.TextField(blank=True)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcoursup.Etudiant', verbose_name='étudiant')),
                ('proposition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parcoursup.Proposition')),
            ],
        ),
    ]
