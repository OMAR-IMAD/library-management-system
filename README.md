Türkçe Açıklama 
Kütüphane Yönetim Sistemi
Açıklama

Kütüphane Yönetim Sistemi, FastAPI ile oluşturulmuş bir arka uç REST API projesidir.

Sistem, kullanıcıların kayıt olmalarına, giriş yapmalarına, kitapları yönetmelerine, kitap ödünç alıp iade etmelerine, rezervasyon oluşturmalarına ve kütüphane istatistiklerini görüntülemelerine olanak tanır.

Özellikler
Kullanıcı kaydı
JWT kimlik doğrulaması ile kullanıcı girişi
Güvenli parola karma algoritması
Kitap yönetimi CRUD
Kitap arama
Sayfalama
Kitap ödünç alma
Kitap iade etme
Ödünç alma geçmişi
Gecikmiş kitaplar
Rezervasyon sistemi
Kütüphane istatistikleri
Docker desteği
Swagger API dokümantasyonu
Kullanılan Teknolojiler
Python
FastAPI
SQLAlchemy
SQLite
JWT Kimlik Doğrulaması
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
POST /kitaplar/
GET /kitaplar/
GET /kitaplar/arama/
GET /kitaplar/{isbn}
PUT /kitaplar/{isbn}
DELETE /kitaplar/{isbn}
Ödünç Alma
POST /ödünç Alma/
POST /ödünç Alma/iade-kitap
GET /ödünç Alma/aktif
GET /ödünç Alma/geçmiş
Rezervasyonlar
POST /rezervasyonlar/
GET /rezervasyonlar/
DELETE /rezervasyonlar/{rezervasyon_id}
İstatistikler
GET /istatistikler/kitaplar
GET /istatistikler/kullanıcılar
GET /istatistikler/ödünç Alınanlar
Projeyi Yerel Olarak Çalıştır
uvicorn app.main:app --reload

Ardından açın:

http://127.0.0.1:8000/docs
Docker ile Çalıştır
docker compose up --build

Ardından Erişim adresi:

http://127.0.0.1:8000/docs
Veritabanı

Proje SQLite veritabanı kullanmaktadır.

Yazar

OMAR IMAD ISMAEL AL-HADEETHI


İngilizce Açıklama 

Library Management System
Description

Library Management System is a backend REST API project built with FastAPI.
The system allows users to register, login, manage books, borrow and return books, create reservations, and view library statistics.

Features
User registration
User login with JWT authentication
Secure password hashing
Book management CRUD
Search books
Pagination
Borrow books
Return books
Borrow history
Overdue books
Reservation system
Library statistics
Docker support
Swagger API documentation
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
