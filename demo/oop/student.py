class Student:
    # static attribute or class attributes
    courses = {"python": 10000, "java": 15000, 'datascience': 20000}

    @staticmethod
    def getfee(course):
        return Student.courses[course]

    # constructor
    def __init__(self, admno, name, course='python'):
        if course not in Student.courses:
            raise ValueError('Invalid Course!')

        # object attributes
        self.admno = admno
        self.name = name
        self.course = course
        self.feepaid = 0

    def payment(self, amount):
        self.feepaid += amount

    def gettotalfee(self):
        return Student.courses[self.course]

    def getdue(self):
        return self.gettotalfee() - self.feepaid

    def __str__(self):
        return f" {self.admno} -  {self.name} - {self.course} - {self.feepaid}"


st1 = Student(1, 'Joe')
st1.payment(3000)
print(st1)
print(st1.getdue())

st2 = Student(2, 'Adams', 'java')
st2.payment(10000)
st2.payment(5000)
print(st2.getdue())

print(Student.getfee('python'))
