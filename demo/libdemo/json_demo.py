import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Person1", 20)
print(p.__dict__)
print(json.dumps(p.__dict__))

persons = [Person("Person1", 20), Person("Person2", 30)]

persons_dict = [p.__dict__ for p in persons]

print(json.dumps(persons_dict))
