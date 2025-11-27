from flask import Flask, request
from db import db, Student

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

db.init_app(app)
with app.app_context():
    db.create_all()


def response_wrapper(success: bool, message: str, data=None):
    return {
        "success": success,
        "message": message,
        "data": data
    }



@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()

    student_list = [
        {
            "id": s.id,
            "name": s.name,
            "age": s.age,
            "email": s.email
        } for s in students
    ]

    return response_wrapper(True, "Students fetched successfully", student_list)



@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get(id)

    if not student:
        return response_wrapper(False, "Student not found"), 404

    return response_wrapper(True, "Student fetched successfully", {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "email": student.email
    })



@app.route("/students", methods=["POST"])
def post_students():
    data = request.get_json()

    new_student = Student(
        name=data["name"],
        age=data["age"],
        email=data["email"]
    )

    db.session.add(new_student)
    db.session.commit()

    return response_wrapper(True, "Student created successfully", {
        "id": new_student.id,
        "name": new_student.name,
        "age": new_student.age,
        "email": new_student.email
    }), 201



@app.route("/students/<int:id>", methods=["PUT"])
def update_age(id):
    data = request.get_json()
    student = Student.query.get(id)

    if not student:
        return response_wrapper(False, "Student not found"), 404

    if "age" not in data:
        return response_wrapper(False, "Only 'age' can be updated"), 400

    student.age = data["age"]
    db.session.commit()

    return response_wrapper(True, "Age updated successfully", {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "email": student.email
    })



@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get(id)

    if not student:
        return response_wrapper(False, "Student not found"), 404

    db.session.delete(student)
    db.session.commit()

    return response_wrapper(True, "Student deleted successfully")
    

if __name__ == "__main__":
    app.run(debug=True)

