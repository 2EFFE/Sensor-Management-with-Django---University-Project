# Generated by Django 5.1.4 on 2024-12-13 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestioneSensori', '0004_alter_letture_options_alter_sensori_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='letture',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='sensori',
            options={'managed': True},
        ),
    ]
