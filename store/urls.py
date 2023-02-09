from django.urls import path, include
from store import views

urlpatterns = [
    path('', views.home, name="home"),
    path('store/', views.store, name="store"),
    path('store/<slug:category_slug>/', views.store, name="products_by_category"),
    path('store/<slug:category_slug>/<slug:product_slug>/', views.product_details, name="product_details"),

    # path('cart/', views.cart, name="cart"),
    # path('caheckout/', views.checkout, name="checkout"),

]