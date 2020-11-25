import json

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from pfp_dapp.models import CityAddress, DepartamentAddress


class UrlDataLoadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    request_path = serializers.CharField(max_length=500)

    def create(self, validated_data):
        file_list = ["/pfp_dapp/load/", "/pfp_dapp/load-dep/"]
        serializer = None
        if self == file_list[0]:
            f = open("pfp_dapp/virtual_city_data.json", 'r')
            dict_data = json.loads(f.read())
            f.close()
            for i in dict_data:
                address = str()
                house_number = str()
                c = 0
                for j in i:
                    if j != ",":
                        address += j
                        c += 1
                    else:
                        break
                c += 1
                house_number += i[c: len(i)]
                stores = dict_data.get(i)[0]
                latitude = dict_data.get(i)[1]
                longitude = dict_data.get(i)[2]
                res = {"ca_address": address,
                       "ca_house_number": house_number,
                       "ca_stores": stores,
                       "ca_latitude": latitude,
                       "ca_longitude": longitude}
                serializer = LoadCityAddressSerializer(data=res)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        elif self == file_list[1]:
            f = open("pfp_dapp/virtual_departament_data.json", 'r')
            dict_data = json.loads(f.read())
            f.close()
            for i in dict_data:
                address = str()
                house_number = str()
                c = 0
                for j in i:
                    if j != ",":
                        address += j
                        c += 1
                    else:
                        break
                c += 1
                house_number += i[c: len(i)]
                latitude = dict_data.get(i)[0]
                longitude = dict_data.get(i)[1]
                rapid = dict_data.get(i)[2]
                big_tank = dict_data.get(i)[3]
                small_ladder = dict_data.get(i)[4]
                big_ladder = dict_data.get(i)[5]
                chemical = dict_data.get(i)[6]
                res = {"dep_address": address,
                       "dep_house_number": house_number,
                       "dep_latitude": latitude,
                       "dep_longitude": longitude,
                       "dep_rapid": rapid,
                       "dep_big_tank": big_tank,
                       "dep_small_ladder": small_ladder,
                       "dep_big_ladder": big_ladder,
                       "dep_chemical": chemical}
                serializer = LoadDepartamentSerializer(data=res)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        return serializer.is_valid()


class LoadCityAddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ca_address = serializers.CharField(max_length=150)
    ca_house_number = serializers.IntegerField(min_value=1, max_value=999)
    ca_stores = serializers.IntegerField(min_value=0, max_value=99)
    ca_latitude = serializers.FloatField(min_value=0, max_value=360)
    ca_longitude = serializers.FloatField(min_value=0, max_value=360)

    def create(self, validated_data):
        return CityAddress.objects.create(**validated_data)


class LoadDepartamentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dep_address = serializers.CharField(max_length=150)
    dep_house_number = serializers.IntegerField(min_value=1, max_value=999)
    dep_latitude = serializers.FloatField(min_value=0, max_value=360)
    dep_longitude = serializers.FloatField(min_value=0, max_value=360)
    dep_rapid = serializers.IntegerField(min_value=0, max_value=99)
    dep_big_tank = serializers.IntegerField(min_value=0, max_value=99)
    dep_small_ladder = serializers.IntegerField(min_value=0, max_value=99)
    dep_big_ladder = serializers.IntegerField(min_value=0, max_value=99)
    dep_chemical = serializers.IntegerField(min_value=0, max_value=99)

    def create(self, validated_data):
        return DepartamentAddress.objects.create(**validated_data)


class CityAddressSerializerPost(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ca_address = serializers.CharField(max_length=150)
    ca_house_number = serializers.IntegerField(min_value=1, max_value=999)
    ca_stores = serializers.IntegerField(min_value=0, max_value=99)
    ca_latitude = serializers.FloatField(min_value=0, max_value=360)
    ca_longitude = serializers.FloatField(min_value=0, max_value=360)

    def create(self, validated_data):
        return CityAddress.objects.create(**validated_data)


class CityAddressSerializerGet(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ca_address = serializers.CharField(max_length=150)
    ca_house_number = serializers.IntegerField(min_value=1, max_value=999)

    def validate(self, attr):
        res = CityAddress.objects\
                .filter(ca_address=attr.get('ca_address'),
                        ca_house_number=attr.get('ca_house_number'))
        if res.exists():
            list_res = list()
            for i in res:
                list_res.append(i)
            dict_res = {"id": list_res[0].id,
                        "ca_address": list_res[0].ca_address,
                        "ca_house_number": list_res[0].ca_house_number,
                        "ca_stores": list_res[0].ca_stores,
                        "ca_latitude": list_res[0].ca_latitude,
                        "ca_longitude": list_res[0].ca_longitude}
            return [dict_res]
        else:
            raise ValidationError(detail="Object was not found.")

    # def update(self, instance, validated_data):
    #     CityAddress.objects.filter(pk=instance.id).update(**validated_data)
    #     return CityAddress.objects.get(pk=instance.pk)


class DepartamentAddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dep_address = serializers.CharField(max_length=150)
    dep_latitude = serializers.FloatField(min_value=0, max_value=360)
    dep_longitude = serializers.FloatField(min_value=0, max_value=360)
