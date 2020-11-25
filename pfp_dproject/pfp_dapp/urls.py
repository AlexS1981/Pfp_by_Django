from django.conf.urls import url
from pfp_dapp.views import CityAddressAPI, UrlDataLoadAPI

urlpatterns = [
    # Отключение возможности загрузки через API
    # url(r'load/', UrlDataLoadAPI.as_view()),
    # url(r'load-dep/', UrlDataLoadAPI.as_view()),

    # Пустой параметр "all_data" возвращает все адреса
    url(r'adress/', CityAddressAPI.as_view())
]