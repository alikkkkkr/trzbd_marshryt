from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'MyApp/index.html')


def user_acc(request):
    return render(request, 'MyApp/user_account.html')


def catalog(request):
    return render(request, 'MyApp/catalog.html')


def basket(request):
    return render(request, 'MyApp/basket.html')


def api(request):
    return render(request, 'MyApp/api.html')
