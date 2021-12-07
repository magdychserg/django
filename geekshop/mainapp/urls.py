from django.urls import path

from mainapp.views import index, products, ProductDeatail

app_name = 'products'
urlpatterns = [

    path('products/', products, name='products'),
    path('category/<int:id_category>', products, name='category'),
    path('page/<int:page>', products, name='page'),
    path('detail/<int:pk>/', ProductDeatail.as_view(), name='detail'),

]
