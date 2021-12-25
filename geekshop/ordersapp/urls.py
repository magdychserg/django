from django.urls import path

from ordersapp.views import OrderList, OrderRead, OrderDelete, OrderUpdate, order_forming_complete, get_product_price, \
    OrderCreate

app_name = 'ordersapp'
urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    path('create/', OrderCreate.as_view(), name='create'),
    path('forming_complete/<int:pk>/', order_forming_complete, name='forming_complete'),
    path('read/<int:pk>/', OrderRead.as_view(), name='read'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('product/<int:pk>/price/', get_product_price, name="product_price"),

]
