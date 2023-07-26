from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from products.models import ProductCategory, Product, Basket


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


@login_required
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)
    

@login_required
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    
    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    elif basket.quantity == 1:
        basket.delete()
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))