from abc import abstractmethod, ABC


# Abstract class
class Doctor(ABC):
    def __init__(self, name, dept, mobile):
        self.name = name
        self.dept = dept
        self.mobile = mobile

    def __str__(self):
        return f"{self.name} - {self.dept} - {self.mobile}"

    @abstractmethod
    def getsalary(self):
        pass


class ResidentDoctor(Doctor):
    def __init__(self, name, dept, mobile, salary):
        super().__init__(name, dept, mobile)
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()} - {self.salary}"

    def getsalary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, dept, mobile, visits, charge):
        super().__init__(name, dept, mobile)
        self.visits = visits
        self.charge = charge

    def __str__(self):
        return f"{super().__str__()} - {self.visits} - {self.charge}"

    def getsalary(self):
        return self.visits * self.charge


r = ResidentDoctor("Dr. Andy", "Card", "3939933333", 300000)
print(r, r.getsalary())

c = Consultant("Dr. James", "Gyn", "3343434343", 10, 1000)
print(c, c.getsalary())
