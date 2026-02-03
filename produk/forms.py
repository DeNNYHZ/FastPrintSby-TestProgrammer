from decimal import Decimal

from django import forms
from .models import Produk


class ProdukForm(forms.ModelForm):
    harga = forms.CharField(
        label="Harga",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Contoh: 10.000",
            "inputmode": "numeric",
            "autocomplete": "off",
        }),
    )

    class Meta:
        model = Produk
        fields = ["nama_produk", "harga", "kategori", "status"]
        widgets = {
            "nama_produk": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Masukkan nama produk",
            }),
            "kategori": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {"nama_produk": "Nama Produk", "kategori": "Kategori", "status": "Status"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.harga is not None:
            self.initial["harga"] = self.instance.harga_display

    def clean_nama_produk(self):
        nama_produk = self.cleaned_data.get("nama_produk")
        if not nama_produk or not nama_produk.strip():
            raise forms.ValidationError("Nama produk harus diisi.")
        return nama_produk.strip()

    def clean_harga(self):
        raw = self.cleaned_data.get("harga")
        if raw is None or (isinstance(raw, str) and not raw.strip()):
            raise forms.ValidationError("Harga harus diisi.")
        if isinstance(raw, str):
            s = raw.replace(".", "").strip()
            if not s.isdigit():
                raise forms.ValidationError("Harga harus berupa angka.")
            raw = Decimal(s)
        if raw <= 0:
            raise forms.ValidationError("Harga harus lebih besar dari 0.")
        return raw
