class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # Private attribute

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __int__(self):
        return self.age

    def __str__(self):
        return f"{self.name} - {self.age}"


p1 = Person("Abc", 20)  # p1.__init__()
p2 = Person("Abc", 20)
p3 = Person("Abc", 30)
print(p1 == p2)  # p1.__eq__(p2)
print(p1 != p2)
# print(p3 > p2)  # p3.__gt__(p2)

print(int(p1) + int(p2))  # p1.__int__()

persons = [p1, p2, p3, Person("Xyz", 15)]

for p in sorted(persons):
    print(p)
