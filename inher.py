# Parent class
class Person:
    def display_name(self):
        print("Name: Rahul")
        print("Age: 20")

# Child class
class Student(Person):
    def display_marks(self):
        print("Marks: 85")

# Create object
s = Student()

# Calling parent class method
s.display_name()

# Calling child class method
s.display_marks()