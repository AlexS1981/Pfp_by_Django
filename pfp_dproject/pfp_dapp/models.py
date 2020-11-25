from django.db import models


# Create your models here.


class CityAddress(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    ca_address = models.CharField(verbose_name='Адреса', max_length=150, blank=False)
    ca_house_number = models.CharField(verbose_name='Номер будинку', max_length=150, blank=False)
    ca_stores = models.CharField(verbose_name='Кількість поверхів', max_length=2, blank=False)
    ca_latitude = models.CharField(verbose_name='Широта', max_length=30, blank=False)
    ca_longitude = models.CharField(verbose_name='Довгота', max_length=30, blank=False)

    def __str__(self):
        return "id {}: ___ {}, {}".format(self.id, self.ca_address, self.ca_house_number)


class DepartamentAddress(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    dep_address = models.CharField(verbose_name='Адреса', max_length=150, blank=False)
    dep_house_number = models.CharField(verbose_name='Номер будинку', max_length=150, blank=False)
    dep_latitude = models.CharField(verbose_name='Широта', max_length=30, blank=False)
    dep_longitude = models.CharField(verbose_name='Довгота', max_length=30, blank=False)
    dep_rapid = models.CharField(verbose_name='_____ АВТОМОБІЛІВ _____:\n- швидкого реагування', max_length=2, blank=False)
    dep_big_tank = models.CharField(verbose_name='- з великою ємністю', max_length=2, blank=False)
    dep_small_ladder = models.CharField(verbose_name='- з драбиною, до 5-ти поверхів', max_length=2, blank=False)
    dep_big_ladder = models.CharField(verbose_name='- з драбиною, до 10-ти поверхів', max_length=2, blank=False)
    dep_chemical = models.CharField(verbose_name='- з хімічними засобами пожежогасіння', max_length=2, blank=False)

    def __str__(self):
        return "id {}: ___ {}, {}".format(self.id, self.dep_address, self.dep_house_number)


class Emergency(models.Model):
    var_type = ["Пожежа у будинку",  # здание
                "Пожежа підчас ДТП",  # транспорт
                "Пожежа на підприємстві",  # предприятие (большая емкость)
                "Пожежа за наявності химічних речовин"]  # химикаты
    EM_TYPE_CHOICES = [
        (var_type[0], var_type[0]),
        (var_type[1], var_type[1]),
        (var_type[2], var_type[2]),
        (var_type[3], var_type[3]),
    ]
    id = models.AutoField(primary_key=True)
    em_address = models.CharField(verbose_name='Адреса', max_length=150, blank=False)
    em_house_number = models.CharField(verbose_name='Номер будинку', max_length=150, blank=False)
    em_type = models.CharField(verbose_name='Тип ЧС', max_length=40, choices=EM_TYPE_CHOICES, default=var_type[0])
    em_date_created = models.DateField(auto_now_add=True)
    em_time_created = models.TimeField(auto_now_add=True)
    em_activated = models.BooleanField(verbose_name='Виконується зараз.', default=True, editable=True)
    em_list_resources = models.CharField(max_length=5, default="00000", editable=False)

    def __str__(self):
        return "Адреса ЧС: {}, {} / Тип: {} / Дата: {} / Час: {}"\
            .format(self.em_address, self.em_type, self.em_house_number, self.em_date_created,
                    self.em_time_created.isoformat(timespec='seconds'))

