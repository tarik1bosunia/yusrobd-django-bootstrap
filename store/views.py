from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from store.models import Product
from category.models import Category
from cart.models import Cart, CartItem
from cart.views import _cart_id


def store(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True).order_by('-id')
        products_count = products.count()

        # pagination
        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('-id')
        products_count = products.count()

        # pagination
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

    context = {
        'categories': categories,
        'category': category,
        "products": paged_products,
        "products_count": products_count,
    }
    return render(request, "store/store.html", context)


def product_details(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        isProductInCart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
    except Exception as e:
        raise e
    context = {
        "product": product,
        "isProductInCart": isProductInCart,
    }
    return render(request, "store/product_details.html", context)
