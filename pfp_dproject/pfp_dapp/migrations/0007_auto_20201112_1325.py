# Generated by Django 3.1.3 on 2020-11-12 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pfp_dapp', '0006_auto_20201112_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentadress',
            name='dep_adress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pfp_dapp.cityadress'),
        ),
    ]
