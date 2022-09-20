class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # Private attribute


p1 = Person("Abc", 20)
print(p1.__dict__)   # get attributes of object
#print(p1.__age)
print(p1._Person__age)
