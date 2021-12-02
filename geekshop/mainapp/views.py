from django.shortcuts import render
import json
import os

from django.views.generic import DetailView

from .models import Product, ProductCategory
MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
def index(request):
    context = {
        'title' : 'Geekshop'

    }
    return render(request, 'mainapp\index.html', context)


def products(request):
    #file_path = os.path.join(MODULE_DIR, 'fixtures/products.json')
    context = {
        'title': 'Geekshop- catalog',
        'products': Product.objects.all(),
        'productscategories' : ProductCategory.objects.all()
    }
   # context['products'] = json.load(open(file_path, encoding = 'utf-8'))

    return render(request, 'mainapp\products.html', context)
class ProductDeatail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDeatail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context

