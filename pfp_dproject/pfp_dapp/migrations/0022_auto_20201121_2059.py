# Generated by Django 3.1.3 on 2020-11-21 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfp_dapp', '0021_auto_20201121_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityadress',
            name='ca_house_number',
            field=models.CharField(default=1, max_length=4, verbose_name='Номер будинку'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departamentadress',
            name='dep_house_number',
            field=models.CharField(default=1, max_length=4, verbose_name='Номер будинку'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emergency',
            name='em_house_number',
            field=models.CharField(default=1, max_length=4, verbose_name='Номер будинку'),
            preserve_default=False,
        ),
    ]
