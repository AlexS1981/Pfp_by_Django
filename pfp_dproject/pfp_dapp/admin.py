from django.contrib import admin

# Register your models here.
from pfp_dapp.models import CityAdress, DepartamentAdress


@admin.register(CityAdress)
class CityAdressAdmin(admin.ModelAdmin):
    pass

@admin.register(DepartamentAdress)
class DepartamentAdressAdmin(admin.ModelAdmin):
    pass