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

# 🚀 **Features Implemented**

### ✔ **1. REST API Using Python (Flask)**

The API is fully REST-compliant:

* Uses proper HTTP verbs (GET, POST, PUT, DELETE)
* Proper status codes
* JSON-based communication

---

### ✔ **2. CRUD Operations**

The following operations are supported:

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| GET    | `/students`      | Fetch all students       |
| GET    | `/students/<id>` | Fetch a specific student |
| POST   | `/students`      | Create a new student     |
| PUT    | `/students/<id>` | Update **only age**      |
| DELETE | `/students/<id>` | Remove a student         |

---

### ✔ **3. Update Only Age (Business Constraint)**

By design, the API restricts updates so that:

* **Only age can be modified**
* Attempts to update name/email return an error

This is enforced inside the PUT route:

---

### ✔ **4. SQLite Database**

The project uses SQLite for simplicity.
SQLAlchemy creates `students.db` automatically.

Config:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
```

---

### ✔ **5. OOPS Principles**

The project applies OOPS through:

* **Student Model class** inside `db.py`
* Encapsulation of fields
* ORM (SQLAlchemy) provides an object-based abstraction over database operations

Model example:

```python
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
```

---

### ✔ **6. REST Principles (RMM Level 2)**

The API adheres to Level 2 of the **Richardson Maturity Model**:

#### **Level 0:** Request-response

#### **Level 1:** Resources

* `/students`
* `/students/<id>`

#### **Level 2:** HTTP Methods + Status Codes

* GET, POST, PUT, DELETE
* 200, 201, 404, 400

---

### ✔ **7. Standardized Response Wrapper (Important Requirement)**

Every response follows a single consistent structure:

```python
def response_wrapper(success: bool, message: str, data=None):
    return {
        "success": success,
        "message": message,
        "data": data
    }
}
```

# 📡 **API Endpoints**

### **1. Create Student**

```
POST /students
```

Body:

```json
{
  "name": "Vishruth",
  "age": 22,
  "email": "vish@example.com"
}
```

---

### **2. Get All Students**

```
GET /students
```

---

### **3. Get Student By ID**

```
GET /students/1
```

---

### **4. Update Only Age**

```
PUT /students/1
```

Body:

```json
{
  "age": 23
}
```

---

### **5. Delete Student**

```
DELETE /students/1
```

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
