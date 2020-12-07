
# Create your views here.
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from pfp_dapp.models import CityAddress, Emergency
from pfp_dapp.serializers import UrlDataLoadSerializer, CityAddressSerializerGet, CityAddressSerializerPost, \
    EmergencySerializerGet, EmergencySerializerPost, EmergencySerializerPostAll


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
            return Response([CityAddressSerializerPost(i).data for i in instance])
        else:
            raise ValidationError(detail="Parameters was not correct.")

    def post(self, request):
        serializer = CityAddressSerializerPost(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(CityAddressSerializerPost(instance).data)


class EmergencyAPI(APIView):

    def get(self, request):
        serializer = EmergencySerializerGet(data=request.GET)
        serializer.is_valid(raise_exception=True)
        instance = serializer.validate(request.GET)
        return Response([CityAddressSerializerPost(i).data for i in instance])

    def post(self, request):
        serializer = EmergencySerializerPost(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = CityAddress.objects \
            .filter(ca_address=request.data.get('em_address'),
                    ca_house_number=request.data.get('em_house_number'))
        for i in res:
            em_dict = i.__dict__
            em_dict.pop('_state')
            em_dict.pop('id')
            em_dict['em_address'] = em_dict.pop('ca_address')
            em_dict['em_house_number'] = em_dict.pop('ca_house_number')
            em_dict['em_type'] = request.data.get('em_address')
            em_dict['em_stores'] = em_dict.pop('ca_stores')
            em_dict['em_latitude'] = em_dict.pop('ca_latitude')
            em_dict['em_longitude'] = em_dict.pop('ca_longitude')
            print(em_dict)
        serializer_all = EmergencySerializerPostAll(data=em_dict)
        serializer_all.is_valid(raise_exception=True)
        instance = serializer_all.save()
        return Response(EmergencySerializerPost(instance).data)
