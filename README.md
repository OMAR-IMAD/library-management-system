# Library Management System

---

# Türkçe Açıklama

## Kütüphane Yönetim Sistemi

### Açıklama

Kütüphane Yönetim Sistemi, FastAPI kullanılarak geliştirilmiş bir REST API projesidir.

Bu sistem kullanıcı kayıtlarını, giriş ve çıkış işlemlerini, kitap yönetimini, ödünç alma ve iade işlemlerini, rezervasyonları ve kütüphane istatistiklerini yönetmektedir.

Ayrıca CSV veri aktarımı desteği ile büyük kitap veri setleri sisteme yüklenebilmektedir.

---

## Özellikler

### Kullanıcı Yönetimi

* Kullanıcı Kaydı
* JWT ile Kullanıcı Girişi
* Kullanıcı Çıkışı (Logout)
* Güvenli Parola Şifreleme
* Rol Yönetimi

### Kitap Yönetimi

* Kitap Ekleme
* Kitap Güncelleme
* Kitap Silme
* ISBN ile Kitap Bulma
* Kitap Arama
* Sayfalama (Pagination)

### Ödünç Alma Sistemi

* Kitap Ödünç Alma
* Kitap İade Etme
* Aktif Ödünçler
* Ödünç Geçmişi
* Gecikmiş Kitaplar

### Rezervasyon Sistemi

* Rezervasyon Oluşturma
* Rezervasyon Listeleme
* Rezervasyon İptali

### İstatistikler

* Toplam Kitap Sayısı
* Toplam Kullanıcı Sayısı
* Toplam Ödünç Alma Sayısı
* En Çok Ödünç Alınan Kitaplar
* Aktif Kullanıcılar
* Aylık Ödünç Alma İstatistikleri

### Veri Aktarma

* CSV Dosyasından Veri Aktarma
* Books Dataset Entegrasyonu
* 27.000+ Kitap Kaydı

### Ek Özellikler

* Swagger API Dokümantasyonu
* Docker Desteği
* GitHub Versiyon Kontrolü

---

## Kullanılan Teknolojiler

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* Passlib (Bcrypt)
* Docker
* GitHub

---

## Proje Yapısı

app/

├── auth/

├── database/

├── models/

├── routers/

├── schemas/

├── services/

└── main.py

---

## API Uç Noktaları

### Users

* POST /users/register
* POST /users/login
* POST /users/logout
* GET /users/

### Books

* POST /books/
* GET /books/
* GET /books/search/
* GET /books/{isbn}
* PUT /books/{isbn}
* DELETE /books/{isbn}

### Borrow

* POST /borrow/
* POST /borrow/return-book
* GET /borrow/active
* GET /borrow/history
* GET /borrow/overdue

### Reservations

* POST /reservations/
* GET /reservations/
* DELETE /reservations/{reservation_id}

### Statistics

* GET /stats/books
* GET /stats/users
* GET /stats/borrows
* GET /stats/most-borrowed
* GET /stats/active-users
* GET /stats/monthly-borrows

---

## Projeyi Yerel Olarak Çalıştırma

```bash
uvicorn app.main:app --reload
```

Ardından:

http://127.0.0.1:8000/docs

---

## Docker ile Çalıştırma

```bash
docker compose up --build
```

Ardından:

http://127.0.0.1:8000/docs

---

## Veritabanı

Bu proje SQLite veritabanı kullanmaktadır.

---

## Yazar

OMAR IMAD ISMAEL AL-HADEETHI

Ostim Teknik Üniversitesi

IYD328 Workplace Experience Project

---

# English Documentation

## Library Management System

### Description

Library Management System is a REST API project developed using FastAPI.

The system allows users to register, login, logout, manage books, borrow and return books, create reservations, and view library statistics.

The project also supports importing large book datasets from CSV files.

---

## Features

### User Management

* User Registration
* JWT Authentication Login
* User Logout
* Secure Password Hashing
* Role Management

### Book Management

* Create Books
* Update Books
* Delete Books
* Search Books
* Find Books by ISBN
* Pagination Support

### Borrowing System

* Borrow Books
* Return Books
* Active Borrows
* Borrow History
* Overdue Books

### Reservation System

* Create Reservations
* View Reservations
* Cancel Reservations

### Statistics

* Total Books
* Total Users
* Total Borrows
* Most Borrowed Books
* Active Users
* Monthly Borrow Statistics

### Dataset Import

* CSV Import Support
* Books Dataset Integration
* 27,000+ Imported Books

### Additional Features

* Swagger API Documentation
* Docker Support
* GitHub Version Control

---

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* Passlib (Bcrypt)
* Docker
* GitHub

---

## Project Structure

app/

├── auth/

├── database/

├── models/

├── routers/

├── schemas/

├── services/

└── main.py

---

## API Endpoints

### Users

* POST /users/register
* POST /users/login
* POST /users/logout
* GET /users/

### Books

* POST /books/
* GET /books/
* GET /books/search/
* GET /books/{isbn}
* PUT /books/{isbn}
* DELETE /books/{isbn}

### Borrow

* POST /borrow/
* POST /borrow/return-book
* GET /borrow/active
* GET /borrow/history
* GET /borrow/overdue

### Reservations

* POST /reservations/
* GET /reservations/
* DELETE /reservations/{reservation_id}

### Statistics

* GET /stats/books
* GET /stats/users
* GET /stats/borrows
* GET /stats/most-borrowed
* GET /stats/active-users
* GET /stats/monthly-borrows

---

## Run Locally

```bash
uvicorn app.main:app --reload
```

Open:

http://127.0.0.1:8000/docs

---

## Run with Docker

```bash
docker compose up --build
```

Open:

http://127.0.0.1:8000/docs

---

## Database

This project uses SQLite database.

---

## Author

OMAR IMAD ISMAEL AL-HADEETHI

Ostim Technical University

IYD328 Workplace Experience Project
