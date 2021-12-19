from django.urls import path

from ordersapp.views import OrderList, OrderRead, OrderDelete, OrderUpdate, order_forming_complete, OrderItemsCreat, get_product_price

app_name = 'ordersapp'
urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),
    path('create/', OrderItemsCreat.as_view(), name='order_create'),
    path('forming/complete<int:pk>/', order_forming_complete, name='order_forming_complete'),
    path('read/<int:pk>/', OrderRead.as_view(), name='order_read'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='order_delete'),
    path('product/<int:pk>/price/', get_product_price, name="product_price"),

]
