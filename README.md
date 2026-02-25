# Flask Users API

A modular Flask REST API for managing users, built with Blueprints and clean project architecture.

This project is part of my backend engineering practice, focusing on:

* Modular Flask architecture
* REST API design
* Docker containerization
* PostgreSQL integration
* AWS deployment (EC2 + RDS)

---

## 🚀 Tech Stack

* Python 3.9+
* Flask
* Flask Blueprints
* Virtual Environments (venv)
* PostgreSQL (planned integration)
* Docker (planned containerization)
* AWS EC2 (planned deployment)
* AWS RDS (planned database)

---

## 📁 Project Structure

```
users_app/
│
├── app.py
├── requirements.txt
├── models/
├── routes/
├── services/
├── serializers/
└── .gitignore
```

* **routes/** → API endpoints (Blueprints)
* **services/** → Business logic layer
* **models/** → Data layer (ORM models)
* **serializers/** → Data transformation layer

This structure follows separation of concerns principles.

---

## ⚙️ Setup Instructions (Local Development)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/gustavomarsan/flask-users-api.git
cd flask-users-api
```

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
flask run
```

API will be available at:

```
http://127.0.0.1:5000
```

---

## 🧪 Example Endpoint

```
GET /users
```

Returns list of users in JSON format.

---

## 🔜 Roadmap

* [ ] Add PostgreSQL integration
* [ ] Dockerize application
* [ ] Run container locally
* [ ] Deploy to AWS EC2
* [ ] Configure AWS RDS (PostgreSQL)
* [ ] Add CI/CD pipeline (GitHub Actions)

---

## 👨‍💻 Author

Gustavo Martinez
Backend Developer | Python | Django | Flask | AWS (Learning)

---

## 📌 License

This project is for educational and portfolio purposes.
