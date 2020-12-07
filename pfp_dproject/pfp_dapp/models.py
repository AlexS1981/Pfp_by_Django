from django.db import models

# Create your models here.



class CityAddress(models.Model):
    ca_address = models.CharField(verbose_name='Адреса', max_length=150, blank=False)
    ca_house_number = models.CharField(verbose_name='Номер будинку', max_length=150, blank=False)
    ca_stores = models.CharField(verbose_name='Кількість поверхів', max_length=2, blank=False)
    ca_latitude = models.CharField(verbose_name='Широта', max_length=30, blank=False)
    ca_longitude = models.CharField(verbose_name='Довгота', max_length=30, blank=False)

    def __str__(self):
        return "id {}: ___ Адреса: {}, {}".format(self.id, self.ca_address, self.ca_house_number)


class DepartamentAddress(models.Model):
    dep_address = models.CharField(verbose_name='Адреса', max_length=150, blank=False)
    dep_house_number = models.CharField(verbose_name='Будинок', max_length=150, blank=False)
    dep_latitude = models.CharField(verbose_name='Широта', max_length=30, blank=False)
    dep_longitude = models.CharField(verbose_name='Довгота', max_length=30, blank=False)
    dep_rapid = models.CharField(verbose_name='Шв. реагування', max_length=2, blank=False)
    dep_big_tank = models.CharField(verbose_name='З ємністю', max_length=2, blank=False)
    dep_small_ladder = models.CharField(verbose_name='З драбиною 5 пов.', max_length=2, blank=False)
    dep_big_ladder = models.CharField(verbose_name='З драбиною 10 пов.', max_length=2, blank=False)
    dep_chemical = models.CharField(verbose_name='З хім. засобами', max_length=2, blank=False)

    class Meta:
        ordering = ("dep_address", "dep_house_number", "id")

    def __str__(self):
        return "id {}: ___ Адреса МНС: {}, {}".format(self.id, self.dep_address, self.dep_house_number)


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
    em_address = models.CharField(verbose_name='Адреса', max_length=150, blank=False)
    em_house_number = models.CharField(verbose_name='Номер будинку', max_length=150, blank=False)
    em_type = models.CharField(verbose_name='Тип ЧС', max_length=40, choices=EM_TYPE_CHOICES, default=var_type[0])
    em_stores = models.CharField(verbose_name='Кількість поверхів', max_length=2, blank=False)
    em_latitude = models.CharField(verbose_name='Широта', max_length=30, blank=False)
    em_longitude = models.CharField(verbose_name='Довгота', max_length=30, blank=False)
    em_date_created = models.DateField(auto_now_add=True)
    em_time_created = models.TimeField(auto_now_add=True)
    em_activated = models.BooleanField(verbose_name='Виконується зараз.', default=True, editable=True)
    em_dep_resources = models.CharField(max_length=150, default="No departament", editable=False)
    em_list_resources = models.CharField(max_length=7, default="00000", editable=False)

    def __str__(self):
        return "id {}: ___ Адреса НС: {}, {} / Тип: {} / Дата: {} / Час: {} / {}"\
            .format(self.id, self.em_address, self.em_house_number, self.em_type, self.em_date_created,
                    self.em_time_created.isoformat(timespec='seconds'), self.em_activated)

