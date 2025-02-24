"""
CLASS Student
ATTRIBUTES:
    students - dict - holds a dictionary of all students (id: Student)
    _id - int - unique - set internally - counts max id in current dict and assigns next number
    _first_name - string - the student's first name
    _last_name - string - the student's last name
    _age - int - the student's age
    _grade - string - A/B/C/D/F - max 1 char

GETTERS AND SETTERS:
    GET id
    GET first_name
    SET first_name
        Must be a string, alpha, no numbers or special characters, greater than 3 chars
    GET last_name
    SET last_name
        Must be a string, alpha, no numbers or special characters, greater than 3 chars
    GET age
    GET grade
    SET grade
        One character string, must be A, B, C, D, F, format - upper

METHODS:
    #get_all_students - class method
        return a list of all Student objects
    
    #get_student_by_id - class method
        Input id
        return a single Student object
    
    #add_student - class method
        input Student object

"""

class Student():
    students = {}

    def __init__(self,id,first_name,last_name,age,grade):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._grade = grade

    # GETTERS AND SETTERS
    @property
    def id(self):
        return self._id
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        # if not isinstance(name, str):
        #     raise ValueError(f"\u001b[31;1m[Invalid Input]\u001b[0m The value for first_name must be a string.")
        # if len(name) < 3:
        #     raise ValueError(f"\u001b[31;1m[Invalid Input]\u001b[0m The value for first_name must be at least three characters in length.")
        # if not name.isalpha():
        #     raise ValueError(f"\u001b[31;1m[Invalid Input]\u001b[0m The value for first_name must not contain any special characters or numbers.")
        self._first_name = name.capitalize().strip()
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    @property
    def age(self):
        return self._age
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def __repr__(self):
        return f"{self._first_name} {self._last_name}"

    def __str__(self):
        return f"ID: {self._id}\n{self._first_name} {self._last_name}\nAge: {self._age}\nGrade: {self._grade}\n"
    
    def to_dict(self):
        return {
            'id': '1', 
            'first_name': self._first_name, 
            'last_name': self._last_name, 
            'age': self._grade, 
            'grade': self._grade
        }
    
    @classmethod
    def get_all_students(cls):
        student_list = []
        for student in cls.students:
            student_list.append(student)
        return student_list
    
    @classmethod
    def get_student_by_id(cls, id):
        # if not isinstance(id, int):
        #     raise ValueError(f"\u001b[31;1m[Invalid Input]\u001b[0m The value for first_name must be a non-negative number.")
        student = cls.students.get(id)
        if not student:
            print(f"\u001b[31;1mStudent with ID {id} not found.\u001b[0m")
            return None
        return student

    
    @classmethod
    def add_student(cls, student):
        if not isinstance(student, Student):
            raise ValueError(f"\u001b[31;1m[Invalid Input]\u001b[0m add_student requires a Student object.")
        cls.students[student.id] = student
        print(f"\u001b[32;1mSUCCESS - STUDENT RECORD ADDED -\u001b[0m [{student.id}] {student.first_name} {student.last_name}")
        return student