# 🎨 Design Asset Bundle Manager API

RESTful API berbasis **FastAPI** untuk mengelola aset desain grafis seperti font, icon, template, dan lainnya dalam satu sistem katalog terstruktur.

---

## 📌 Deskripsi Proyek

Aplikasi ini dikembangkan sebagai bagian dari **Proyek UTS Pemrograman Web Lanjutan** dengan tujuan membangun sistem backend berbasis **microservice sederhana** menggunakan FastAPI.

Sistem ini memungkinkan pengguna untuk:

* Mengelola kategori aset
* Menambahkan dan mengelola aset desain
* Mengelompokkan aset menggunakan tag
* Mengamankan endpoint dengan autentikasi JWT

---

## 🚀 Teknologi yang Digunakan

* **FastAPI** – Web framework utama
* **SQLAlchemy** – ORM database
* **SQLite** – Database lokal
* **Pydantic** – Validasi data
* **JWT (JSON Web Token)** – Autentikasi
* **Uvicorn** – ASGI server

---

## 📂 Struktur Proyek

```
design_asset_manager/
├── main.py
├── database.py
├── models/
│   ├── user.py
│   ├── category.py
│   ├── asset.py
│   └── tag.py
├── schemas/
│   ├── user.py
│   ├── category.py
│   ├── asset.py
│   └── tag.py
├── routers/
│   ├── auth.py
│   ├── category.py
│   ├── asset.py
│   └── tag.py
├── auth/
│   ├── jwt_handler.py
│   ├── auth_bearer.py
│   └── utils.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Cara Menjalankan Project

### 1. Clone repository

```bash
git clone https://github.com/username/design-asset-manager.git
cd design-asset-manager
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan server

```bash
uvicorn main:app --reload
```

### 4. Buka Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Autentikasi (JWT)

### Register

```http
POST /auth/register
```

### Login

```http
POST /auth/login
```

Response:

```json
{
  "access_token": "your_token",
  "token_type": "bearer"
}
```

### Gunakan Token

Klik tombol **🔓 Authorize** di Swagger lalu isi:

```
Bearer your_token
```

---

## 📊 Fitur Utama

### 👤 User

* Register
* Login (JWT)

### 📂 Category

* Create Category 🔒
* Get All Category
* Get Category by ID
* Update Category 🔒
* Delete Category 🔒

### 🎨 Asset

* Create Asset 🔒
* Get All Asset
* Get Asset by ID
* Update Asset 🔒
* Delete Asset 🔒

### 🏷️ Tag

* Create Tag 🔒
* Get All Tag
* Get Tag by ID
* Update Tag 🔒
* Delete Tag 🔒

🔒 = membutuhkan autentikasi JWT

---

## 🔗 Relasi Database

* **User → Asset** (One-to-Many)
* **Category → Asset** (One-to-Many)
* **Asset ↔ Tag** (Many-to-Many)

---

## 🧪 Testing

### Menggunakan Swagger UI

* Akses `/docs`
* Coba semua endpoint
* Gunakan token JWT untuk endpoint protected

### Menggunakan Postman

* Import collection
* Test semua endpoint (termasuk JWT)

---

## 📌 HTTP Status Code

| Status | Keterangan       |
| ------ | ---------------- |
| 200    | OK               |
| 201    | Created          |
| 401    | Unauthorized     |
| 403    | Forbidden        |
| 404    | Not Found        |
| 422    | Validation Error |

---

## 🔥 Fitur Tambahan

* Validasi input dengan Pydantic
* Proteksi endpoint dengan JWT
* Relasi database kompleks (Many-to-Many)
* Error handling (404, 401, 403)

---

## 👨‍💻 Author

Nama: **[Erly Winarni]**
NIM: **[H071241074]**

---

## 📄 Lisensi

Project ini dibuat untuk keperluan akademik (UTS Pemrograman Web Lanjutan).
