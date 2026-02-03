from django.db import models


class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True, db_column="id_kategori")
    nama_kategori = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'produk_kategori'
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategori'

    def __str__(self):
        return self.nama_kategori


class Status(models.Model):
    id_status = models.AutoField(primary_key=True, db_column="id_status")
    nama_status = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'produk_status'
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.nama_status


class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=12, decimal_places=2)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, db_column='kategori_id')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, db_column='status_id')

    class Meta:
        db_table = 'produk_produk'
        verbose_name = 'Produk'
        verbose_name_plural = 'Produk'

    def __str__(self):
        return self.nama_produk

    @property
    def harga_display(self):
        s = str(int(self.harga))
        parts = []
        for i, c in enumerate(reversed(s)):
            if i and i % 3 == 0:
                parts.append(".")
            parts.append(c)
        return "".join(reversed(parts))
