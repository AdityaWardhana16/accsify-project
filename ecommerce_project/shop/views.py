from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Kategori, Product, Cart, Order, OrderItem
from django.http import Http404

class KategoriListView(ListView):
    model = Kategori
    template_name = 'shop/kategori_list.html'
    context_object_name = 'kategoris'

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

class CartDetailView(DetailView):
    model = Cart
    template_name = 'shop/cart_detail.html'
    context_object_name = 'cart'

    def get_object(self):
        user = self.request.user
        try:
            return Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            raise Http404("Cart does not exist")

class OrderListView(ListView):
    model = Order
    template_name = 'shop/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDetailView(DetailView):
    model = Order
    template_name = 'shop/order_detail.html'
    context_object_name = 'order'

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise Http404("You are not authorized to view this order.")
        return obj
