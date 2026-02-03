from django.urls import path
from .views import *

urlpatterns = [
    path('', produk_list, name='produk_list'),
    path('sync/', sync_produk, name='sync_produk'),
    path('tambah/', tambah_produk, name='tambah_produk'),
    path('edit/<int:id>/', edit_produk, name='edit_produk'),
    path('hapus/<int:id>/', hapus_produk, name='hapus_produk'),
]
