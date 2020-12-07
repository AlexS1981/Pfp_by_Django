from django.conf.urls import url


from pfp_dapp.views import CityAddressAPI, UrlDataLoadAPI, EmergencyAPI

urlpatterns = [
    # Отключение возможности загрузки через API
    # url(r'load/', UrlDataLoadAPI.as_view()),
    # url(r'load-dep/', UrlDataLoadAPI.as_view()),

    # Пустой параметр "all_data" возвращает все адреса
    url(r'address/', CityAddressAPI.as_view()),
    url(r'emergency/', EmergencyAPI.as_view())
]