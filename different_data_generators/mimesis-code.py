from mimesis import Person
import random
person = Person()

print("First Name:", person.first_name())
print("Last Name:", person.last_name())
print("Email:", person.email())
print("Phone:", person.telephone())
print("Age:", random.randint(18, 65))