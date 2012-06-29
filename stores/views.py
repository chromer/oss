from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Store, Brand, Product


def home(request):
    '''
    Renders home page for OSS.
    '''
    stores = Store.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    return render_to_response('home.html', RequestContext(request, {
        'stores': stores,
        'brands': brands,
        'products': products,
    }))


def stores(request):
    '''
    List view for all the stores.
    '''
    pass


def brands(request):
    '''
    List view for all the brands.
    '''
    pass


def products(request):
    '''
    List view for all the products.
    '''
    pass