from django.urls import path, include
from store import views

urlpatterns = [
    path('', views.store, name="store"),
    path('<slug:category_slug>/', views.store, name="products_by_category"),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_details, name="product_details"),

    # path('cart/', views.cart, name="cart"),
    # path('caheckout/', views.checkout, name="checkout"),

]