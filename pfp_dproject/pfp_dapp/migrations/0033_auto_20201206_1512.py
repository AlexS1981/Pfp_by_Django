# Generated by Django 3.1.3 on 2020-12-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfp_dapp', '0032_auto_20201206_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityaddress',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='departamentaddress',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='emergency',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]