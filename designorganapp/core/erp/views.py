from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Estados

# Create your views here.
def myferstview (request):
    data = {
        'name': 'Loco Maxi',
        'States': Estados.objects.all()
    }
    return render(request,'index.html', data)


def mysecondview (request):
    data = {
        'name': 'Maxi',
        'States': Estados.objects.all()
    }
    return render(request,'index.html', data)
