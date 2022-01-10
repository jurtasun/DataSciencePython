# Data science in Python course
# Jesus Urtasun - January 2021
# Week 1 - exercise 1

print("Data science in Python")
print("Week 1 - exercise 1")

# Objects in Python
print("\nObjects in Python")

class Person:

    department = "Bioinformatics"

    def set_name(self, new_name):
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location

# Instanciate the class
person = Person()
person.set_name("Jesus Urtasun")
person.set_location("London, UK")
print("{} lives in {} and works in the {} deparment".format(person.name, person.location, person.department))

# Lambda expressions
print("\nLambda expressions")

# Example 1
my_function = lambda a, b, c, : a + b
my_function(1, 2, 3)

# Example 2
people = ["Dr. Yi-Fang Wang", "Dr. Jesus Urtasun", "Dr. Giancarlo Ferrera"]

# Convert the following expression into a lambda
def split_title_and_name(person):
    return person.split()[0] + " " + person.split()[-1]

# option 1
# for person in people:
#     print(split_title_and_name(person) == lambda x: x.split()[0] + " " + x.split()[-1])

# option 2
# for person in people:
#     print(map(split_title_and_name(person)) == list(map(lambda x: x.split()[0] + " " + x.split()[-1])))

# List comprehensions
print("\nList comprehensions")

my_list1 = []
for number in range(0, 100):
    if number % 2 == 0:
        my_list1.append(number)
print("my list 1 \n", my_list1)

my_list2 = [number for number in range(0, 100) if number % 2 == 0]
print("my list 2 \n", my_list2)