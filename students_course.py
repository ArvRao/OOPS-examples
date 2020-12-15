class Student:
    def __init__(self, name, age, course_grade, gender):
        self.name=name
        self.age=age
        self.course_grade=course_grade
        self.gender=gender
    
    def grade(self):
        return self.course_grade


class Course:
    def __init__(self,name, max_students):
        self.name=name
        self.max_students=max_students
        self.students = []  # stores all students in this course

    def add_students(self,student): # student will be instance of student object
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def average_grade(self):
        value = 0

        for student in self.students:
            value += student.grade()
        
        return value / len(self.students)

s1 = Student('Arvind',21,100,'M')
s2 = Student('Nagesh',21,82,'M')
s3 = Student('Ravikant',21,80,'M')

course = Course('Computers',2)
course.add_students(s1)
course.add_students(s2)
print(course.students[0].name)

print(course.average_grade())