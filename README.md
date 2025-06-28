# Flask Simple Login App

Aplikasi login sederhana menggunakan Flask dan Flask-Login.  
User akan diarahkan ke dashboard sesuai role (admin/user) setelah login.

## Fitur
- Login dengan username & password
- Redirect otomatis ke dashboard sesuai role
- Pesan error jika login gagal
- Tombol lihat/sembunyikan password
- Tampilan modern & responsif (Bootstrap + custom CSS)
- Logout

## Struktur Folder
```
flash login/
├── falshlogin.py
├── css/
│   └── style.css
├── html/
│   ├── login.html
│   ├── admin.html
│   └── user.html
└── README.md

## Cara Menjalankan
1. Install dependensi:
    ```
    pip install flask flask-login
    ```
2. Jalankan aplikasi:
    ```
    python falshlogin.py
    ```
3. Buka browser ke:
    ```
    http://127.0.0.1:5000/
    ```

## User Login
- **admin** / **123** (dashboard admin)
- **user** / **123** (dashboard user)

## Catatan
- Semua file HTML ada di folder `html`
- Semua file CSS ada di folder `css`
- Untuk produksi, sebaiknya gunakan database untuk user, bukan dictionary

---

**Selamat mencoba!**