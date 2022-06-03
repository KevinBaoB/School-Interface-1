from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Student.all_students()
        self.students = Staff.all_staff()

    @property
    def get_name(self):
        return self.name

    @property
    def get_staff(self):
        return self.staff
    
    @property
    def get_students(self):
        return self.students
    
    def __repr__(self):
        return f"The school {self.name}."

school = School('High')
print(school.students)