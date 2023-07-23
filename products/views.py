from django.shortcuts import render

from products.models import ProductCategory, Product

# Create your views here.

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)


def test_context(request):
    context = {
        'title': 'store',
        'header': 'Добро пожаловать!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи', 'price': 6900.00},
            {'name': 'Синяя куртка', 'price': 9000.00},
            {'name': 'Коричневый рюкзак', 'price': 3200.00},
        ],
        'promotion': True,
        'products_of_promotion':[
            {'name': 'Черный рюкзак', 'price': 3000.00},
        ]
    }
    return render(request, 'products/test-context.html', context)