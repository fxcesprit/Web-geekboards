from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('.well-known/appspecific/com.chrome.devtools.json', views.chrome_devtools),
]