from rest_framework import serializers

from pfp_dapp.models import CityAdress


class CityAdressSerializer(serializers.Serializer):
    ca_id = serializers.IntegerField(read_only=True)
    ca_adress = serializers.CharField(max_length=150, blank=False)
    ca_stores = serializers.IntegerField(localize=True)
    ca_latitude = serializers.FloatField(blank=False, localize=True)
    ca_longitude = serializers.FloatField(blank=False, localize=True)

    # def create(self, validated_data):
    #     return CityAdress.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     CityAdress.objects.filter(pk=instance.id).update(**validated_data)
    #     return CityAdress.objects.get(pk=instance.pk)

class DepartamentAdressSerializer(serializers.Serializer):
    dep_id = serializers.IntegerField(read_only=True)
    dep_adress = serializers.CharField(max_length=150, blank=False)
    dep_latitude = serializers.FloatField(blank=False, localize=True)
    dep_longitude = serializers.FloatField(blank=False, localize=True)
