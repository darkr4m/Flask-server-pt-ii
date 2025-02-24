"""
API ENDPOINTS
/old_students/
    Return list of student objects older than 20
/youung_students/
    Return list of student objects younger than 21
/advance_students/
    Return list of student objects younger than 21 and have letter grade of 'A'
/student_names/
    Return list of student objects by first_name and last_name
/student_ages/
    Return list of student objects with student name and age
/students/
    Return list of all student objects

Student Class
    id - integer
    first_name - string
    last_name - string
    age - integer
    grade - string
"""
from flaskr.classes.student import Student
# sample student data
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

# student = Student(**students[0])
# print(student)
# Student.add_student(student)

for student in students:
    new_student = Student(**student)
    Student.add_student(new_student)

stud1 = Student.get_student_by_id('1')
print(stud1)
stud2 = print(Student.get_student_by_id('2'))

print(stud1.to_dict())