# Generated by Django 4.0.6 on 2022-07-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoire', '0006_alter_utilisateur_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50, null=True)),
            ],
            options={
                'ordering': ['nom', '-prenom'],
            },
        ),
        migrations.DeleteModel(
            name='Utilisateur',
        ),
    ]
