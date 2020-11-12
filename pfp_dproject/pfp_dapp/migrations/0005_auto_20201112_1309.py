# Generated by Django 3.1.3 on 2020-11-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfp_dapp', '0004_auto_20201112_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamentadress',
            name='dep_latitude',
            field=models.FloatField(default=1, verbose_name='Широта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departamentadress',
            name='dep_longitude',
            field=models.FloatField(default=2, verbose_name='Довгота'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cityadress',
            name='ca_adress',
            field=models.CharField(max_length=150, verbose_name='Адреса'),
        ),
        migrations.AlterField(
            model_name='cityadress',
            name='ca_latitude',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='cityadress',
            name='ca_longitude',
            field=models.FloatField(verbose_name='Довгота'),
        ),
        migrations.AlterField(
            model_name='cityadress',
            name='ca_stores',
            field=models.IntegerField(default=0, verbose_name='Кількість поверхів'),
        ),
        migrations.AlterField(
            model_name='departamentadress',
            name='dep_adress',
            field=models.CharField(max_length=150, verbose_name='Адреса'),
        ),
    ]
