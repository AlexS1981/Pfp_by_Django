
# Create your views here.
from io import BytesIO

from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from pfp_dapp.models import CityAddress
from pfp_dapp.serializers import UrlDataLoadSerializer, CityAddressSerializerGet, CityAddressSerializerPost


class UrlDataLoadAPI(APIView):

    def post(self, request):
        url_path = {'request_path': request.path}
        serializer = UrlDataLoadSerializer(data=url_path)
        serializer.is_valid(raise_exception=True)
        resp = UrlDataLoadSerializer.create(request.path, request.data)
        res = 'Loading was not perfect. Incorrect data...'
        if resp == False:
            print(res)
            raise ValidationError(res)
        else:
            fl = ["/pfp_dapp/load/", "/pfp_dapp/load-dep/",
                "City data was loaded.", "Departament data was loaded."]
            if request.path == fl[0]:
                res = fl[2]
            elif request.path == fl[1]:
                res = fl[3]
        # Выводим в терминал
        print(res)
        # Выводим в Response
        return Response(res)


class CityAddressAPI(APIView):

    def get(self, request):
        if request.GET.get("all_data") == str():
            return Response(CityAddressSerializerPost(CityAddress.objects.all(), many=True).data)
        elif request.GET:
            serialiser = CityAddressSerializerGet(data=request.GET)
            serialiser.is_valid(raise_exception=True)
            instance = serialiser.validate(attr=request.GET)
            return Response(instance)
        else:
            raise ValidationError(detail="Parameters was not correct.")

    # def post(self, request):
    #     serializer = CityAddressSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     instance = serializer.save()
    #     # instance = CityAdress.objects.create(**request.data)
    #     return Response(CityAddressSerializer(instance).data)



