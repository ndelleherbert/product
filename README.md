# FastAPI + PostgreSQL + SQLAlchemy Project

This project is a clean and well-structured FastAPI application connected to a PostgreSQL database using SQLAlchemy ORM. It includes a database configuration module, ORM models, an application entry point, and can be easily extended with CRUD routers, schemas, and services.

---

## 📌 Overview

This project demonstrates how to build a modern backend API using:

* **FastAPI** (high-performance ASGI framework)
* **PostgreSQL** (robust relational database)
* **SQLAlchemy ORM** (database models + engine + sessions)
* **Uvicorn** (ASGI server)

The codebase is modular, easy to maintain, and ready for production enhancements.

---

## 📁 Project Structure

```
project/
│
├── database.py          # Database engine, SessionLocal, Base
├── models.py            # SQLAlchemy ORM models
├── main.py              # FastAPI entry point
├── crud.py              # (Optional) CRUD logic
├── routers/             # (Optional) Route modules
├── schemas.py           # (Optional) Pydantic models
└── requirements.txt
```

---

## ⚙️ Installation & Setup

Follow the steps below to run the application.

### **1. Clone the project**

```
git clone <your-repo-url>
cd project
```

### **2. Create and activate a virtual environment**

```
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### **3. Install dependencies**

```
pip install -r requirements.txt
```

### **4. Install PostgreSQL**

Make sure PostgreSQL is installed and running on your machine.

Create the database:

```
createdb -U postgres product
```

Or using pgAdmin: create a database named **product**.

---

## 🛠️ Configuration

### **database.py** contains the DB connection:

```
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/product"
```

Update username, password, and database if needed.

---

## 🧱 Database Models

Example `Product` model:

```
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
```

SQLAlchemy will generate the table automatically on startup.

---

## ▶️ Running the Application

Start the server with:

```
uvicorn main:app --reload
```

Access the API documentation:

* Interactive Swagger UI → **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
* ReDoc → **[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)**

---

## 📚 API Endpoints

### Default endpoint

```
GET /
Response: { "message": "Hello, Welcome to our application" }
```

Additional endpoints will be added through routers.

---

## 🧩 Adding CRUD Functionality (Optional)

You can expand the project using the following modules:

### **schemas.py** → Request/response Pydantic models

### **crud.py** → Create, Read, Update, Delete operations

### **routers/** → API routing modules

Example Product CRUD operations can easily be added.

---

## 📝 Recommended Git Commit Messages

```
git add database.py
git commit -m "Add PostgreSQL configuration and SQLAlchemy Base setup"

git add models.py
git commit -m "Define Product model and database schema"

git add main.py
git commit -m "Initialize FastAPI app and create database tables"
```

---

## 🚀 Deployment

You can deploy using:

* Docker & Docker Compose
* Render
* Fly.io
* Railway
* DigitalOcean Apps
* AWS EC2 / Lightsail

Add environment variables:

```
DATABASE_URL=postgresql://USER:PASS@HOST:PORT/DBNAME
```

---

## 🤝 Contributing

Pull requests are welcome! Ensure code is typed, formatted, and logically organized.

---

## 📄 License

This project can be adapted or reused freely.

---

If you want, I can also generate:

* CRUD endpoints
* Authentication (JWT)
* A production-ready Dockerfile
* An extended README with diagrams
