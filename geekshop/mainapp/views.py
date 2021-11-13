from django.shortcuts import render


# Create your views here.
def index(request):
    return render(index, 'index.html')


def products(request):
    return render(products, 'products.html')
