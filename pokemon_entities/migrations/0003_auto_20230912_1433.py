# Generated by Django 3.1.14 on 2023-09-12 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20230912_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='parent',
            new_name='evolution',
        ),
    ]
