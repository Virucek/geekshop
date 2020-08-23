# -*- coding: windows-1251 -*-
import random

from django.shortcuts import render, get_object_or_404
import os
import json

from basketapp.models import Basket
from geekshop import settings
from mainapp.models import ProductCategory, Product


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_same_products(product):
    same_products = Product.objects.filter(category=product.category, is_active=True).exclude(pk=product.pk)[:4]
    return same_products


def get_hot_product():
    products = Product.objects.filter(category__is_active=True, is_active=True)
    return random.sample(list(products), 1)[0]


def main(request):
    content = {
        'title': '������� �����',
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', context=content)


def catalog(request, pk=None):
    if pk == 0 or pk is None:
        catalog_list = Product.objects.filter(category__is_active=True, is_active=True).order_by('price')
        title = '������� �������'
    else:
        curr_category = get_object_or_404(ProductCategory, pk=pk, is_active=True)
        catalog_list = Product.objects.filter(category=pk, is_active=True).order_by('price')
        title = curr_category.name
    submenu_list = ProductCategory.objects.filter(is_active=True)

    content = {
        'title': title,
        'catalog_list': catalog_list,
        'submenu_list': submenu_list,
        'basket': get_basket(request.user),
        'hot_product': get_hot_product(),
    }
    return render(request, 'mainapp/catalog.html', context=content)


def contacts(request):
    with open(os.path.join(settings.BASE_DIR, "address.json"), "r", encoding="utf8") as file:
        json_data = json.load(file)

    content = {
        'title': '��������',
        'address_data': json_data,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contacts.html', context=content)


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True, category__is_active=True)
    title = f'�������: {product.name}'
    submenu_list = ProductCategory.objects.filter(is_active=True)
    content = {
        'title': title,
        'product': product,
        'submenu_list': submenu_list,
        'basket': get_basket(request.user),
        'same_products': get_same_products(product),
    }
    return render(request, f'mainapp/product_detail.html', context=content)
