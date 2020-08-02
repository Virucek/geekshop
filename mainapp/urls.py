from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp
from geekshop import settings

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.catalog, name='cat_index'),
    path('<int:pk>', mainapp.catalog, name='catalog'),
]
