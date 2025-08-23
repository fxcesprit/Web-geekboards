from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chrome_devtools(request):
    return HttpResponse(status=204)

def index(request):
    return HttpResponse("<h4>app works</h4>")
