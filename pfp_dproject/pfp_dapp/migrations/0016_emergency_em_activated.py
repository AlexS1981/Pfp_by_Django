# Generated by Django 3.1.3 on 2020-11-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfp_dapp', '0015_auto_20201120_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergency',
            name='em_activated',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]