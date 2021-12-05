from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import  reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCategoryEditForm, ProductEditForm
from authapp.models import User
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from mainapp.models import Product, ProductCategory


# Пользователи

class AdminListView(TemplateView, BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'admins/admin.html'
    title = 'Админка '

class UserListView(ListView, BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Админка | Пользователи'


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Создание пользователя'


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Редактирование пользователя'


class UserDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Удаление пользователя'



# Категории

class CategoriesListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories.html'
    title = 'Админка | Категории'

class CategoriesCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = ProductCategoryEditForm
    success_url = reverse_lazy('admins:admin_categories')
    title = 'Админка | Создание категории'


class CategoriesUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = ProductCategoryEditForm
    success_url = reverse_lazy('admins:admin_categories')
    title = 'Админка | Редактирование категории'

class CategoriesDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    success_url = reverse_lazy('admins:admin_categories')
    title = 'Админка | Удаление категории'


# Продукты
class ProductListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products.html'
    title = 'Админка | Продукты'

class ProductCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Админка | Создание Продукты'

class ProductUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Админка | Редактирование Продукты'

class ProductDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')
    title = 'Админка | Удаление Продукты'
