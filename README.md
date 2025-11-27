# Student Management REST API

A simple, clean, beginner-friendly **Python Flask REST API** implementing complete CRUD operations for a **Student** table with a constraint that **only age can be updated**.

This project demonstrates:

* REST API development using **Flask**
* **SQLite** database handling using SQLAlchemy ORM
* **OOPS principles** via models + service-like organizational structure
* **RMM Level 2** REST maturity
* A **standardized response wrapper**
* Clean routing and proper HTTP status codes
* Structured code for maintainability

---

# 🗄️ **Database Design**

### **Students Table**

| Column | Type            | Description                  |
| ------ | --------------- | ---------------------------- |
| id     | Integer (PK)    | Auto-incremented primary key |
| name   | String          | Student's name               |
| age    | Integer         | Student's age                |
| email  | String (unique) | Student's email              |

---

### ✔ **CRUD Operations**

The following operations are supported:

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| GET    | `/students`      | Fetch all students       |
| GET    | `/students/<id>` | Fetch a specific student |
| POST   | `/students`      | Create a new student     |
| PUT    | `/students/<id>` | Update **only age**      |
| DELETE | `/students/<id>` | Remove a student         |

---


# ▶️ **How to Run**

### 1. Install dependencies:

```bash
pip install flask flask_sqlalchemy
```

### 2. Run the server:

```bash
python main.py
```

### 3. The API runs at:

```
http://localhost:5000
```

---

# 🎯 Conclusion

This project demonstrates:

* Clean REST API design
* SQLAlchemy ORM
* Strict update constraints
* Standard response formatting
* REST maturity (RMM Level 2)
* OOP-compliant model structure
