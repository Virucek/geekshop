from django.shortcuts import render
import os
import json

from geekshop import settings
from mainapp.models import ProductCategory, Product


def main(request):
    content = {
        'title': 'магазин мерча',
    }
    return render(request, 'mainapp/index.html', context=content)

def catalog(request):
    """
    catalog_list = [
        {
            'href': 'detail',
            'product_name': 'overwatch',
            'img': 'img/poster_overwatch.jpg',
            'text': 'Постер по видеоигре Overwatch',
        },
        {
            'href': 'detail',
            'product_name': 'shawshank',
            'img': 'img/poster_shawshank.jpg',
            'text': 'Постер по кинофильму The Shawshank redemption'
        },
        {
            'href': 'detail',
            'product_name': 'nirvana',
            'img': 'img/poster_nirvana.jpg',
            'text': 'Постер рок-группы Nirvana'
        },

    ]
    """
    with open(os.path.join(settings.BASE_DIR, "catalog_list.json"), "r", encoding="utf8") as file:
        json_data = json.load(file)

    catalog_list = json_data
    for i in catalog_list:
        i.update({"href": "detail"})

    submenu_list = ProductCategory.objects.all()

    content = {
        'title': 'каталог товаров',
        'catalog_list': catalog_list,
        'submenu_list': submenu_list,
    }
    return render(request, 'mainapp/catalog.html', context=content)

def contacts(request):
    with open(os.path.join(settings.BASE_DIR, "address.json"), "r", encoding="utf8") as file:
        json_data = json.load(file)

    content = {
        'title': 'контакты',
        'address_data': json_data
    }
    return render(request, 'mainapp/contacts.html', context=content)

def detail(request, product_name):
    content = {
        'title': 'продукт',
        'product_img': f'img/poster_{product_name}.jpg',
    }
    return render(request, f'mainapp/catalog/{product_name}.html', context=content)