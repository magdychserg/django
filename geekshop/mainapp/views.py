from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
import os
from django.views.generic import DetailView, ListView
from .models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.
def index(request):
    context = {
        'title': 'Geekshop | Главная'

    }
    return render(request, 'mainapp/index.html', context)





def products(request, id_category=None, page=1):

    context = {'title': 'Geekshop | Каталог'}
    if id_category:
        products = Product.objects.filter(category_id=id_category).select_related('category')
    else:
        products = Product.objects.all().select_related('category')
    paginator = Paginator(products, per_page=3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = products_paginator
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)


class ProductDeatail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDeatail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
