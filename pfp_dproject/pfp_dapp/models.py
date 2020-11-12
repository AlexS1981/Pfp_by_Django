from django.db import models

# Create your models here.


class CityAdress(models.Model):
    ca_id = models.AutoField(primary_key=True, blank=False)
    ca_adress = models.CharField(verbose_name='Адреса', max_length=150, blank=False)
    ca_stores = models.IntegerField(verbose_name='Кількість поверхів', blank=False)
    ca_latitude = models.FloatField(verbose_name='Широта', blank=False)
    ca_longitude = models.FloatField(verbose_name='Довгота', blank=False)

    def __str__(self):
        return self.ca_adress


class DepartamentAdress(models.Model):
    dep_id = models.AutoField(primary_key=True, blank=False)
    dep_adress = models.ForeignKey(CityAdress, on_delete=models.CASCADE)
    dep_latitude = CityAdress.ca_latitude
    dep_longitude = CityAdress.ca_longitude

    def __str__(self):
        return self.dep_adress

# class Emergency(models.Model):
#     em_id = models.AutoField(primary_key=True)
#     em_name = models.CharField(max_length=100)
#     em_date_created = models.DateField(auto_now_add=True)
#     em_test_field = models.TextField(blank=True)
#
#     def __str__(self):
#         return "Statistic|{}".format(self.email)
