from django.urls import path
from . import views

urlpatterns = [
    #GET
    path('', views.GetDevicesList, name='devices_list_url'),
    path('device/<int:device_id>', views.GetDeviceInfo, name='device_info_url'),
    path('user_devices', views.GetDevicesBox, name='devices_box_url'),

    #POST
    # path('search_device', views.searchDevice, name='search_device_url'),

    #Other
    path('.well-known/appspecific/com.chrome.devtools.json', views.chrome_devtools), # убирает ошибку GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1 404 2710 при открытии кода страницы
]