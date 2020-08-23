from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryAdminEditForm, ProductAdminEditForm, \
    MerchTypeAdminEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product, MerchType


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['title'] = 'админка / пользователи'

        return context

# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка / пользователи'
#     users_list = ShopUser.objects.all()
#
#     content = {
#         'title': title,
#         'objects': users_list,
#     }
#
#     return render(request, 'adminapp/users.html', context=content)


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')
    form_class = ShopUserRegisterForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        self.context['title'] = 'пользователи / создание'

        return self.context

# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'пользователи / создание'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     content = {
#         'title': title,
#         'update_form': user_form,
#     }
#
#     return render(request, 'adminapp/user_update.html', content)


class UserEditView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')
    form_class = ShopUserAdminEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        self.context['title'] = 'пользователи / редактирование'

        return self.context

# @user_passes_test(lambda u: u.is_superuser)
# def user_edit(request, pk):
#     title = 'пользователи / редактирование'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=user)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         user_form = ShopUserAdminEditForm(instance=user)
#
#     content = {
#         'title': title,
#         'update_form': user_form,
#     }
#
#     return render(request, 'adminapp/user_update.html', content)


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователи / удаление'

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     title = 'пользователи / удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         if user.is_active:
#             user.is_active = False
#         else:
#             user.is_active = True
#         user.save()
#         return HttpResponseRedirect(reverse('admin:users'))
#
#     content = {
#         'title': title,
#         'user_to_delete': user,
#     }
#
#     return render(request, 'adminapp/user_delete.html', content)


class CategoriesListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoriesListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка / категории'
        return context
#
# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     title = 'админка / категории'
#     categories_list = ProductCategory.objects.all()
#     content = {
#         'title': title,
#         'objects': categories_list
#     }
#
#     return render(request, 'adminapp/categories.html', content)


class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории / создание'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     title = 'категории / создание'
#
#     if request.method == 'POST':
#         category_form = ProductCategoryAdminEditForm(request.POST)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         category_form = ProductCategoryAdminEditForm()
#
#     content = {
#         'title': title,
#         'update_form': category_form,
#     }
#
#     return render(request, 'adminapp/category_update.html', content)


class CategoryEditView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории / редактирование'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def category_edit(request, pk):
#     title = 'категории / редактирование'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         category_form = ProductCategoryAdminEditForm(request.POST, instance=category)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         category_form = ProductCategoryAdminEditForm(instance=category)
#
#     content = {
#         'title': title,
#         'update_form': category_form,
#     }
#
#     return render(request, 'adminapp/category_update.html', content)


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории / удаление'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     title = 'категории / удаление'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         if category.is_active:
#             category.is_active = False
#         else:
#             category.is_active = True
#         category.save()
#         return HttpResponseRedirect(reverse('admin:categories'))
#
#     content = {
#         'title': title,
#         'category_to_delete': category,
#     }
#
#     return render(request, 'adminapp/category_delete.html', content)


class ProductsListView(ListView):
    paginate_by = 3
    model = Product
    template_name = 'adminapp/products.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории / товары'
        category_pk = self.kwargs['pk']
        print(f'CONTEXT 1111111111_______ {context}')
        context['category'] = ProductCategory.objects.get(pk=category_pk)
        print(f'CONTEXT 2222222222_______ {context}')
        print(f'CONTEXT 3333333333_______ {context["paginator"]}')
        print(f'CONTEXT 4444444444_______ {context["page_obj"]}')
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk, page=1):
#     title = 'категории / товары'
#     category = get_object_or_404(ProductCategory, pk=pk)
#     products = Product.objects.filter(category__pk=pk)
#     items_on_page = 3
#
#     paginator = Paginator(products, items_on_page)
#     try:
#         paginator_products = paginator.page(page)
#     except PageNotAnInteger:
#         paginator_products = paginator.page(1)
#     except EmptyPage:
#         paginator_products = paginator.page(paginator.num_pages)
#
#     content = {
#         'title': title,
#         'objects': paginator_products,
#         'category': category,
#     }
#
#     return render(request, 'adminapp/products.html', content)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'товар / подробнее'
        print(f'detail___________{context}')
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     title = f'товар / {product_item.name}'
#
#     content = {
#         'title': title,
#         'object': product_item,
#         'category': product_item.category,
#     }
#
#     return render(request, 'adminapp/product.html', content)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    fields = '__all__'

    def get_success_url(self):
        category_id = self.kwargs['pk']
        return reverse_lazy('admin:products', kwargs={'pk': category_id})

    def get_initial(self):
        category = ProductCategory.objects.get(pk=self.kwargs['pk'])
        return {'category': category}

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'товары / создание'
        category_id = self.kwargs['pk']
        context['category'] = ProductCategory.objects.get(pk=category_id)
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     title = 'товары / создание'
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductAdminEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin:products', args=[pk]))
#     else:
#         product_form = ProductAdminEditForm(initial={'category':category})
#
#     content = {
#         'title': title,
#         'update_form': product_form,
#         'category': category,
#     }
#
#     return render(request, 'adminapp/product_update.html', content)


class ProductEditView(UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    fields = '__all__'

    def get_success_url(self):
        product = Product.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('admin:products', kwargs={'pk': product.category.id})

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'товары / редактирование'
        product = Product.objects.get(pk=self.kwargs['pk'])
        context['category'] = product.category
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_edit(request, pk):
#     title = 'товары / редактирование'
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductAdminEditForm(request.POST, request.FILES, instance=product)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))
#     else:
#         product_form = ProductAdminEditForm(instance=product)
#     content = {
#         'title': title,
#         'update_form': product_form,
#         'category': product.category,
#     }
#
#     return render(request, 'adminapp/product_update.html', content)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def get_success_url(self):
        product = Product.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('admin:products', kwargs={'pk': product.category.id})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'товары / удаление'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'товары / удаление'
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         if product.is_active:
#             product.is_active = False
#         else:
#             product.is_active = True
#         product.save()
#         return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))
#     content = {
#         'title': title,
#         'product_to_delete': product,
#         'category': product.category,
#     }
#
#     return render(request, 'adminapp/product_delete.html', content)


class MerchTypesListView(ListView):
    model = MerchType
    template_name = 'adminapp/merch_types.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка / типы мерча'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def merch_types(request):
#     title = 'админка / типы мерча'
#     merch_types_list = MerchType.objects.all()
#     content = {
#         'title': title,
#         'objects': merch_types_list,
#     }
#
#     return render(request, 'adminapp/merch_types.html', content)


class MerchTypeCreateView(CreateView):
    model = MerchType
    template_name = 'adminapp/merch_type_update.html'
    success_url = reverse_lazy('admin:merch_types')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'типы мерча / создание'
        return context
# @user_passes_test(lambda u: u.is_superuser)
# def merch_type_create(request):
#     title = 'типы мерча / создание'
#
#     if request.method == 'POST':
#         mtype_form = MerchTypeAdminEditForm(request.POST)
#         if mtype_form.is_valid():
#             mtype_form.save()
#             return HttpResponseRedirect(reverse('admin:merch_types'))
#     else:
#         mtype_form = MerchTypeAdminEditForm()
#     content = {
#         'title': title,
#         'update_form': mtype_form,
#     }
#
#     return render(request, 'adminapp/merch_type_update.html', content)


class MerchTypeEditView(UpdateView):
    model = MerchType
    template_name = 'adminapp/merch_type_update.html'
    success_url = reverse_lazy('admin:merch_types')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'типы мерча / редактирование'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def merch_type_edit(request, pk):
#     title = 'типы мерча / редактирование'
#     mtype = get_object_or_404(MerchType, pk=pk)
#
#     if request.method == 'POST':
#         mtype_form = MerchTypeAdminEditForm(request.POST, instance=mtype)
#         if mtype_form.is_valid():
#             mtype_form.save()
#             return HttpResponseRedirect(reverse('admin:merch_types'))
#     else:
#         mtype_form = MerchTypeAdminEditForm(instance=mtype)
#     content = {
#         'title': title,
#         'update_form': mtype_form,
#     }
#
#     return render(request, 'adminapp/merch_type_update.html', context=content)


class MerchTypeDeleteView(DeleteView):
    model = MerchType
    template_name = 'adminapp/merch_type_delete.html'
    success_url = reverse_lazy('admin:merch_types')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'типы мерча / удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def merch_type_delete(request, pk):
#     title = 'типы мерча / удаление'
#     mtype = get_object_or_404(MerchType, pk=pk)
#
#     if request.method == 'POST':
#         if mtype.is_active:
#             mtype.is_active = False
#         else:
#             mtype.is_active = True
#         mtype.save()
#         return HttpResponseRedirect(reverse('admin:merch_types'))
#
#     content = {
#         'title': title,
#         'mtype_to_delete': mtype
#     }
#
#     return render(request, 'adminapp/merch_type_delete.html', context=content)