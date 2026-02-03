# Fast Print - Tes Junior Programmer

Aplikasi web untuk mengelola data produk menggunakan Django Framework dengan integrasi API dari Fast Print.

## Deskripsi

Aplikasi ini dibuat untuk memenuhi requirement tes programmer dari Fast Print. Aplikasi dapat mengambil data produk dari API, menyimpan ke database, dan menyediakan fitur CRUD (Create, Read, Update, Delete) untuk mengelola produk.

## Fitur

1. **Sync Data dari API** - Mengambil data produk dari API Fast Print dan disimpan ke database
2. **Tampilkan Produk** - Hanya menampilkan produk dengan status "bisa dijual"
3. **Tambah Produk** - Menambahkan produk baru menggunakan validasi form
4. **Edit Produk** - Mengedit data produk yang sudah ada dengan validasi form
5. **Hapus Produk** - Menghapus produk dengan konfirmasi 

## Teknologi yang Digunakan

- **Framework**: Django 6.0.1
- **Database**: PostgreSQL
- **Python**: 3.13
- **Django REST Framework**: Untuk serializer
- **Bootstrap 5**: Untuk UI

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Konfigurasi Database

Edit file `fastprint/settings.py` dan sesuaikan konfigurasi database:

**PostgreSQL:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fastprint_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**MySQL:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fastprint_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Migrasi

```bash
python manage.py makemigrations
python manage.py migrate
```

### Jalankan Server

```bash
python manage.py runserver
```
## Struktur Database

### Tabel Produk

| Kolom        | Tipe          | Keterangan                          |
|--------------|---------------|-------------------------------------|
| id_produk    | Integer       | Primary Key                         |
| nama_produk  | Varchar(255)  | Nama produk                         |
| harga        | Decimal(12,2) | Harga produk                        |
| kategori_id  | Integer       | Foreign Key ke tabel **Kategori**   |
| status_id    | Integer       | Foreign Key ke tabel **Status**     |

---

### Tabel Kategori

| Kolom          | Tipe          | Keterangan                    |
|----------------|---------------|-------------------------------|
| id_kategori    | Integer       | Primary Key (Auto Increment)  |
| nama_kategori  | Varchar(100)  | Nama kategori (Unique)        |

---

### Tabel Status

| Kolom       | Tipe          | Keterangan                     |
|-------------|---------------|--------------------------------|
| id_status   | Integer       | Primary Key (Auto Increment)   |
| nama_status | Varchar(50)   | Nama status (Unique)           |

## API Integration

Aplikasi mengambil data dari API Fast Print:

**Endpoint:** `https://recruitment.fastprint.co.id/tes/api_tes_programmer`

**Autentikasi:**
- Username: `tesprogrammer{DD}{MM}{YY}C{hh}` 
- Password: MD5 dari `bisacoding-{DD}-{MM}-{YY}`

**Flow:**
1. POST request untuk login dan mendapatkan token
2. GET request dengan Bearer token untuk mengambil data produk

## Penggunaan

### 1. Sync Data dari API

1. Buka halaman utama aplikasi
2. Klik tombol **"Sync dari API"**
3. Data produk akan diambil dan disimpan ke database
4. Produk dengan status "bisa dijual" akan ditampilkan di halaman utama

### 2. Tambah Produk

1. Klik tombol **"+ Tambah Produk"**
2. Isi form:
   - **Nama Produk** (wajib diisi)
   - **Harga** (wajib diisi, harus angka)
   - **Kategori** (pilih dari dropdown)
   - **Status** (pilih dari dropdown)
3. Klik **"Simpan"**

### 3. Edit Produk

1. Di halaman daftar produk, klik tombol **"Edit"** pada produk yang ingin diedit
2. Ubah data yang diperlukan
3. Klik **"Simpan"**

### 4. Hapus Produk

1. Di halaman daftar produk, klik tombol **"Hapus"** pada produk yang ingin dihapus
2. Konfirmasi penghapusan di popup yang muncul
3. Produk akan dihapus dari database

## Validasi Form

- **Nama Produk**: Wajib diisi, tidak boleh kosong
- **Harga**: Wajib diisi, harus berupa angka dan lebih besar dari 0

## Kontak

Untuk pertanyaan atau masalah, silakan hubungi:
- Email: iamdenisetiawan@gmail.com

Project ini dibuat untuk keperluan tes programmer Fast Print.

---

**Catatan:** Pastikan untuk mengganti kredensial database dan konfigurasi sesuai dengan environment Anda sebelum menjalankan aplikasi.
