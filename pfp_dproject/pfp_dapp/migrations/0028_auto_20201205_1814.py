# Generated by Django 3.1.3 on 2020-12-05 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfp_dapp', '0027_auto_20201201_1140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamentaddress',
            options={'ordering': ('dep_address', 'dep_house_number', 'id')},
        ),
        migrations.AddField(
            model_name='departamentaddress',
            name='map_frame',
            field=models.CharField(default='<iframe style="border: 2px solid green;" src="https://www.openstreetmap.org/export/embed.html?bbox={{ box_lat_a }}%2C{{ box_lon_a }}%2C{{ box_lat_b }}%2C{{ box_lon_b }}&amp;layer=transportmap&amp;marker={{ latitude }}%2C{{ longitude }}"width="400px" height="300px" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>', editable=False, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='departamentaddress',
            name='dep_big_ladder',
            field=models.CharField(max_length=2, verbose_name='З драбиною 10 пов.'),
        ),
        migrations.AlterField(
            model_name='departamentaddress',
            name='dep_big_tank',
            field=models.CharField(max_length=2, verbose_name='З ємністю'),
        ),
        migrations.AlterField(
            model_name='departamentaddress',
            name='dep_chemical',
            field=models.CharField(max_length=2, verbose_name='З хім. засобами'),
        ),
        migrations.AlterField(
            model_name='departamentaddress',
            name='dep_house_number',
            field=models.CharField(max_length=150, verbose_name='Будинок'),
        ),
        migrations.AlterField(
            model_name='departamentaddress',
            name='dep_rapid',
            field=models.CharField(max_length=2, verbose_name='Шв. реагування'),
        ),
        migrations.AlterField(
            model_name='departamentaddress',
            name='dep_small_ladder',
            field=models.CharField(max_length=2, verbose_name='З драбиною 5 пов.'),
        ),
    ]