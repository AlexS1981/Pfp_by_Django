# from django.shortcuts import render


# Create your views here.
import os

import json

from pfp_dapp.models import CityAdress
from pfp_dapp.serializers import CityAdressSerializer


def load_adresses():
    os.chdir(os.getcwd())
    f = open("virtual_city_data.json", 'r')
    str_data = str()
    str_end = str()
    for line in f:
        str_data += line[0: len(line) - 1]
        str_end = line[len(line) - 1:]
    str_data += str_end
    f.close()
    dict_data = json.loads(str_data)
    address_data = dict_data.get("address_data")
    for adress in address_data:
        my_id = 0
        stores = address_data.get(adress)[0]
        latitude = address_data.get(adress)[1]
        longitude = address_data.get(adress)[2]
        request = {"ca_id": my_id,
                   "ca_adress": adress,
                   "ca_stores": stores,
                   "ca_latitude": latitude,
                   "ca_longitude": longitude}
        serializer = CityAdressSerializer(data=request)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance = CityAdress.objects.create(**request)
        my_id += 1


load_adresses()
