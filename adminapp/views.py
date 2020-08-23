from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryAdminEditForm, ProductAdminEditForm, \
    MerchTypeAdminEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product, MerchType


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка / пользователи'
    users_list = ShopUser.objects.all()

    content = {
        'title': title,
        'objects': users_list,
    }

    return render(request, 'adminapp/users.html', context=content)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи / создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {
        'title': title,
        'update_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_edit(request, pk):
    title = 'пользователи / редактирование'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserAdminEditForm(instance=user)

    content = {
        'title': title,
        'update_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи / удаление'

    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {
        'title': title,
        'user_to_delete': user,
    }

    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'админка / категории'
    categories_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'категории / создание'

    if request.method == 'POST':
        category_form = ProductCategoryAdminEditForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        category_form = ProductCategoryAdminEditForm()

    content = {
        'title': title,
        'update_form': category_form,
    }

    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_edit(request, pk):
    title = 'категории / редактирование'

    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category_form = ProductCategoryAdminEditForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        category_form = ProductCategoryAdminEditForm(instance=category)

    content = {
        'title': title,
        'update_form': category_form,
    }

    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'категории / удаление'

    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        if category.is_active:
            category.is_active = False
        else:
            category.is_active = True
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {
        'title': title,
        'category_to_delete': category,
    }

    return render(request, 'adminapp/category_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'категории / товары'
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category__pk=pk)
    content = {
        'title': title,
        'objects': products,
        'category': category,
    }

    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    title = f'товар / {product_item.name}'

    content = {
        'title': title,
        'object': product_item,
        'category': product_item.category,
    }

    return render(request, 'adminapp/product.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'товары / создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductAdminEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        product_form = ProductAdminEditForm(initial={'category':category})

    content = {
        'title': title,
        'update_form': product_form,
        'category': category,
    }

    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_edit(request, pk):
    title = 'товары / редактирование'
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product_form = ProductAdminEditForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))
    else:
        product_form = ProductAdminEditForm(instance=product)
    content = {
        'title': title,
        'update_form': product_form,
        'category': product.category,
    }

    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'товары / удаление'
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        if product.is_active:
            product.is_active = False
        else:
            product.is_active = True
        product.save()
        return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))
    content = {
        'title': title,
        'product_to_delete': product,
        'category': product.category,
    }

    return render(request, 'adminapp/product_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def merch_types(request):
    title = 'админка / типы мерча'
    merch_types_list = MerchType.objects.all()
    content = {
        'title': title,
        'objects': merch_types_list,
    }

    return render(request, 'adminapp/merch_types.html', content)


@user_passes_test(lambda u: u.is_superuser)
def merch_type_create(request):
    title = 'типы мерча / создание'

    if request.method == 'POST':
        mtype_form = MerchTypeAdminEditForm(request.POST)
        if mtype_form.is_valid():
            mtype_form.save()
            return HttpResponseRedirect(reverse('admin:merch_types'))
    else:
        mtype_form = MerchTypeAdminEditForm()
    content = {
        'title': title,
        'update_form': mtype_form,
    }

    return render(request, 'adminapp/merch_type_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def merch_type_edit(request, pk):
    title = 'типы мерча / редактирование'
    mtype = get_object_or_404(MerchType, pk=pk)

    if request.method == 'POST':
        mtype_form = MerchTypeAdminEditForm(request.POST, instance=mtype)
        if mtype_form.is_valid():
            mtype_form.save()
            return HttpResponseRedirect(reverse('admin:merch_types'))
    else:
        mtype_form = MerchTypeAdminEditForm(instance=mtype)
    content = {
        'title': title,
        'update_form': mtype_form,
    }

    return render(request, 'adminapp/merch_type_update.html', context=content)


@user_passes_test(lambda u: u.is_superuser)
def merch_type_delete(request, pk):
    title = 'типы мерча / удаление'
    mtype = get_object_or_404(MerchType, pk=pk)

    if request.method == 'POST':
        if mtype.is_active:
            mtype.is_active = False
        else:
            mtype.is_active = True
        mtype.save()
        return HttpResponseRedirect(reverse('admin:merch_types'))

    content = {
        'title': title,
        'mtype_to_delete': mtype
    }

    return render(request, 'adminapp/merch_type_delete.html', context=content)