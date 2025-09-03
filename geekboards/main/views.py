from django.shortcuts import render
from django.http import HttpResponse

collection = {
    'devices' : [
        {'id': 1, 'name': 'kb1', 'price': 1500, 'short_desc': "kb", 'desc': 'very beautiful kb', 'img': None},
        {'id': 2, 'name': 'kb2', 'price': 15000, 'short_desc': "kb", 'desc': 'very beautiful kb', 'img': None},
        {'id': 3, 'name': 'kb3', 'price': 4600, 'short_desc': "kb", 'desc': 'very beautiful kb', 'img': None},
    ]
}

# Create your views here.
def chrome_devtools(request):
    """убирает ошибку GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1 404 2710 при открытии кода страницы"""
    return HttpResponse(status=204)


def GetDevicesList(request, data=collection):
    """Рендер страницы девайсов + поиск"""
    
    search_text = ''
    
    if request.method == 'POST':
        search_text = request.POST.get('search_text', '').strip()
    
    if search_text:
        filtered_devices = [
            device for device in collection['devices'] 
            if search_text.lower() in device['name'].lower()
        ]
    else:
        filtered_devices = collection['devices']
    
    data = {
        'devices': filtered_devices,
        'search_text': search_text 
    }

    return render(request, 'main/devices_list.html', data)


def GetDeviceInfo(request, device_id, data=collection):
    """Рендер страницы информации о конкретном девайсе"""
    return render(request, 'main/device_info.html', {'device': data['devices'][device_id - 1]})


def GetDevicesBox(request, user_id):
    """Рендер страницы корзины девайсов пользователя"""
    return render(request, 'main/devices_box.html')


# def searchDevice(request):
#     input_text = request.POST['search_text']
#     data = {'devices': [
#         device for device in collection['devices'] if input_text in device['name']
#     ]}
#     return GetDevicesList(request, data)