Library Management System
Türkçe Açıklama
Kütüphane Yönetim Sistemi
Açıklama

Kütüphane Yönetim Sistemi, FastAPI ile geliştirilmiş bir REST API projesidir.

Sistem kullanıcı kayıtlarını, giriş işlemlerini, kitap yönetimini, ödünç alma ve iade işlemlerini, rezervasyonları ve istatistikleri yönetmektedir.

Özellikler
Kullanıcı Kaydı
JWT Kimlik Doğrulama
Güvenli Parola Şifreleme
Kitap CRUD İşlemleri
Kitap Arama
Sayfalama (Pagination)
Kitap Ödünç Alma
Kitap İade Etme
Ödünç Geçmişi
Gecikmiş Kitaplar
Rezervasyon Sistemi
Kütüphane İstatistikleri
CSV Veri Aktarma
Docker Desteği
Swagger API Dokümantasyonu
Kullanılan Teknolojiler
Python
FastAPI
SQLAlchemy
SQLite
JWT Authentication
Docker
GitHub
Proje Yapısı
app/
├── auth/
├── database/
├── models/
├── routers/
├── schemas/
└── main.py
API Uç Noktaları
Kullanıcılar
POST /users/register
POST /users/login
GET /users/
Kitaplar
POST /books/
GET /books/
GET /books/search/
GET /books/{isbn}
PUT /books/{isbn}
DELETE /books/{isbn}
Ödünç Alma
POST /borrow/
POST /borrow/return-book
GET /borrow/active
GET /borrow/history
GET /borrow/overdue
Rezervasyonlar
POST /reservations/
GET /reservations/
DELETE /reservations/{reservation_id}
İstatistikler
GET /stats/books
GET /stats/users
GET /stats/borrows
Veri Seti İçe Aktarma

Proje büyük ölçekli kitap verilerini içe aktarabilmektedir.

books.csv dosyası 270.000'den fazla kitap içermektedir.

Komut:

python import_books.py
Projeyi Yerel Olarak Çalıştır
uvicorn app.main:app --reload

Sonra açın:

http://127.0.0.1:8000/docs
Docker ile Çalıştır
docker compose up --build

Sonra açın:

http://127.0.0.1:8000/docs
Veritabanı

Bu proje SQLite veritabanı kullanmaktadır.

Yazar

OMAR IMAD ISMAEL AL-HADEETHI



English Description
Library Management System
Description

Library Management System is a backend REST API project built with FastAPI.

The system allows users to register, login, manage books, borrow and return books, create reservations, import datasets, and view library statistics.

Features
User Registration
JWT Authentication
Secure Password Hashing
Book CRUD Operations
Search Books
Pagination
Borrow Books
Return Books
Borrow History
Overdue Books
Reservation System
Library Statistics
CSV Dataset Import
Docker Support
Swagger API Documentation
Technologies Used
Python
FastAPI
SQLAlchemy
SQLite
JWT Authentication
Docker
GitHub
Project Structure
app/
├── auth/
├── database/
├── models/
├── routers/
├── schemas/
└── main.py
API Endpoints
Users
POST /users/register
POST /users/login
GET /users/
Books
POST /books/
GET /books/
GET /books/search/
GET /books/{isbn}
PUT /books/{isbn}
DELETE /books/{isbn}
Borrow
POST /borrow/
POST /borrow/return-book
GET /borrow/active
GET /borrow/history
GET /borrow/overdue
Reservations
POST /reservations/
GET /reservations/
DELETE /reservations/{reservation_id}
Statistics
GET /stats/books
GET /stats/users
GET /stats/borrows
Dataset Import

The project includes a dataset import script.

books.csv contains more than 270,000 books.

Run:

python import_books.py
Run Project Locally
uvicorn app.main:app --reload

Then open:

http://127.0.0.1:8000/docs
Run With Docker
docker compose up --build

Then open:

http://127.0.0.1:8000/docs
Database

The project uses SQLite database.

Author

OMAR IMAD ISMAEL AL-HADEETHI
