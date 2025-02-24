from flask import Blueprint, jsonify

# from .classes.student import Student
bp = Blueprint('students',__name__)

students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

@bp.route('/students')
def all_students():
    # Returns an array of all student objects available.
    # students = [student.to_dict() for student in Student.get_all_students()]
    # students = list(map(lambda x: x.to_dict(), Student.get_all_students()))
    return jsonify(students)

@bp.route('/old_students')
def old_students():
    # Returns an array of student objects where the students are older than 20 years old.
    student_list = list(filter(lambda x: x['age'] > 20, students))
    return jsonify(student_list)

@bp.route('/young_students')
def young_students():
    # Returns an array of student objects where the students are younger than 21 years old.
    student_list = list(filter(lambda x: x['age'] < 21, students))
    return jsonify(student_list)

@bp.route('/advance_students')
def adv_students():
    # Returns an array of student objects where the students are younger than 21 and have a letter grade of "A."
    student_list = list(filter(lambda x: x['age'] > 20 and x['grade'] == 'A', students))
    return jsonify(student_list)

@bp.route('/student_names')
# Returns an array of student objects holding only the keys of 'first_name' and 'last_name' along with their corresponding values.
def student_names():
    student_list = [{'first_name': student['first_name'], 'last_name': student['last_name']} for student in students]
    return jsonify(student_list)

@bp.route('/student_ages')
# Returns an array of student objects holding the keys 'student_name' with the value of first and last name, and 'age' with the value of that student's age.
def student_ages():
    student_list = [{'student_name': f'{student['first_name']} {student['last_name']}','age': student['age']} for student in students]
    return jsonify(student_list)
