# Generated by Django 3.1.3 on 2020-11-13 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfp_dapp', '0008_auto_20201112_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cityadress',
            old_name='ca_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='departamentadress',
            old_name='dep_id',
            new_name='id',
        ),
    ]
