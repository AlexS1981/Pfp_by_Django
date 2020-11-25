from django.contrib import admin

# Register your models here.
from pfp_dapp.models import CityAddress, DepartamentAddress, Emergency


@admin.register(CityAddress)
class CityAdressAdmin(admin.ModelAdmin):
    pass

@admin.register(DepartamentAddress)
class DepartamentAdressAdmin(admin.ModelAdmin):
    pass

@admin.register(Emergency)
class EmergencyAdmin(admin.ModelAdmin):
    pass