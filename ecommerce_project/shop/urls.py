from django.urls import path
from . import views

urlpatterns = [
    path('kategori/', views.KategoriListView.as_view(), name='kategori_list'),
    path('produk/', views.ProductListView.as_view(), name='product_list'),
    path('produk/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('keranjang/', views.CartDetailView.as_view(), name='cart_detail'),
    path('pesanan/', views.OrderListView.as_view(), name='order_list'),
    path('pesanan/<int:id>/', views.OrderDetailView.as_view(), name='order_detail'),
]
