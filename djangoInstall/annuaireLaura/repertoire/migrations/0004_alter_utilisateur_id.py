# Generated by Django 4.0.6 on 2022-07-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoire', '0003_rename_repertoire_utilisateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
