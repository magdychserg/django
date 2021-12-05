from django.urls import path

from admins.views import AdminListView, UserListView, UserUpdateView, UserCreateView, UserDeleteView, ProductListView, \
    CategoriesListView, CategoriesCreateView, CategoriesUpdateView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoriesDeleteView

app_name = 'admins'
urlpatterns = [

    path('', AdminListView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),

    path('categories/', CategoriesListView.as_view(), name='admin_categories'),
    path('categories-create/', CategoriesCreateView.as_view(), name='admin_categories_create'),
    path('categories-update/<int:pk>/', CategoriesUpdateView.as_view(), name='admin_categories_update'),
    path('categories-delete/<int:pk>/', CategoriesDeleteView.as_view(), name='admin_categories_delete'),

    path('products/', ProductListView.as_view(), name='admin_products'),
    path('products-create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products-update/<int:pk>/', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products-delete/<int:pk>/', ProductDeleteView.as_view(), name='admin_products_delete'),
]
