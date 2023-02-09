from django.shortcuts import render, get_object_or_404

from store.models import Product
from category.models import Category


def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        "products": products
    }
    return render(request, "home.html", context)


def store(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()

    context = {
        'categories': categories,
        'category': category,
        "products": products,
        "products_count": products_count,
    }
    return render(request, "store/store.html", context)


def product_details(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        "product": product
    }
    return render(request, "store/product_details.html", context)
