from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/', adminapp.users, name='users'),
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/edit/<int:pk>/', adminapp.user_edit, name='user_edit'),
    path('edit/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('categories/', adminapp.categories, name='categories'),
    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/edit/<int:pk>/', adminapp.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),

    path('products/category/<int:pk>/', adminapp.products, name='products'),
    path('products/<int:pk>/', adminapp.product, name='product'),
    path('products/create/category/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/edit/<int:pk>/', adminapp.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),

    path('merchtypes/', adminapp.merch_types, name='merch_types'),
    path('merchtypes/create', adminapp.merch_type_create, name='merch_type_create'),
    path('merchtypes/edit/<int:pk>/', adminapp.merch_type_edit, name='merch_type_edit'),
    path('merchtypes/delete/<int:pk>/', adminapp.merch_type_delete, name='merch_type_delete'),
]
