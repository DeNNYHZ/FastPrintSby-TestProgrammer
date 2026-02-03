from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models

from .forms import ProdukForm
from .models import Produk, Kategori, Status
from .services import fetch_produk

STATUS_BISA_DIJUAL = "bisa dijual"


def sync_produk(request):
    try:
        produk_list = fetch_produk()
    except Exception as e:
        messages.error(request, f"Gagal sync produk: {str(e)}")
        return redirect("produk_list")

    created_count = 0
    updated_count = 0

    for item in produk_list:
        id_barang = int(item.get("id_barang", item.get("id_produk", 0)))
        nama_barang = item.get("nama_barang", item.get("nama_produk", ""))
        kategori_nama = item.get("kategori", "")
        harga = float(item.get("harga", 0))
        status_nama = item.get("status", "")

        kategori_obj, _ = Kategori.objects.get_or_create(nama_kategori=kategori_nama)
        status_obj, _ = Status.objects.get_or_create(nama_status=status_nama)

        _, created = Produk.objects.update_or_create(
            id_produk=id_barang,
            defaults={
                "nama_produk": nama_barang,
                "harga": harga,
                "kategori": kategori_obj,
                "status": status_obj,
            },
        )
        if created:
            created_count += 1
        else:
            updated_count += 1

    messages.success(
        request,
        f"Sync berhasil! {created_count} produk baru, {updated_count} diperbarui.",
    )
    return redirect("produk_list")


def produk_list(request):
    produk = Produk.objects.select_related("kategori", "status").filter(
        status__nama_status=STATUS_BISA_DIJUAL
    ).order_by("id_produk")
    return render(request, "produk/list.html", {"produk": produk})


def tambah_produk(request):
    if not Kategori.objects.exists() or not Status.objects.exists():
        messages.warning(
            request,
            "Belum ada kategori atau status. Sync dari API dulu.",
        )
        return redirect("produk_list")

    form = ProdukForm(request.POST or None)
    if form.is_valid():
        max_id = Produk.objects.aggregate(models.Max("id_produk"))["id_produk__max"] or 0
        produk = form.save(commit=False)
        produk.id_produk = max_id + 1
        produk.save()
        messages.success(request, f"Produk '{produk.nama_produk}' berhasil ditambahkan.")
        return redirect("produk_list")

    return render(request, "produk/form.html", {"form": form, "title": "Tambah Produk"})


def edit_produk(request, id):
    produk = get_object_or_404(Produk, id_produk=id)
    form = ProdukForm(request.POST or None, instance=produk)
    if form.is_valid():
        form.save()
        messages.success(request, "Produk berhasil diperbarui.")
        return redirect("produk_list")
    return render(request, "produk/form.html", {"form": form, "title": "Edit Produk"})


def hapus_produk(request, id):
    produk = get_object_or_404(Produk, id_produk=id)
    if request.method == "POST":
        produk.delete()
        messages.success(request, f"Produk '{produk.nama_produk}' berhasil dihapus.")
        return redirect("produk_list")
    return render(request, "produk/confirm_delete.html", {"produk": produk})