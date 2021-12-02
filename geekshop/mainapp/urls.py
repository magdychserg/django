from django.urls import path

from mainapp.views import index, products, ProductDeatail

app_name = 'products'
urlpatterns = [

    path('products/', products, name='products'),
    path('detail/<int:pk>/', ProductDeatail.as_view(), name='detail'),
]
