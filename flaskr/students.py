from flask import Blueprint, jsonify
from .models.Students import Students

# from .classes.student import Student
bp = Blueprint('students',__name__)

@bp.route('/students')
def all_students():
    students = Students.query.all()
    student_list = [
        {
            'id': student.id,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'age': student.age,
            'grade': student.grade
        } for student in students
    ]
    
    return jsonify(student_list)

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
