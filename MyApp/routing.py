from django.contrib import admin
from django.urls import path
import MyApp.views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', v.index, name='indexPage'),
    path('account/', v.user_acc, name='useraccountPage'),
    path('catalog/', v.catalog, name='catalogPage'),
    path('basket/', v.basket, name='basketPage'),
    path('api/', v.api, name='apiPage'),
]