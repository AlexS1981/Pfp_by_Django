# Generated by Django 3.1.3 on 2020-12-06 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pfp_dapp', '0030_auto_20201206_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergency',
            name='em_address',
            field=models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, to='pfp_dapp.cityaddress', verbose_name='Адреса'),
        ),
    ]