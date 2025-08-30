#program to demonstrate inheritance
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def display_info(self):
        print(f"Name is={self.name}, Age is={self.age}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self.grade=grade
    
    def display_info(self):
        super().display_info()
        print (f"Grade is={self.grade}")

obj1=Student(name="Jaya", age=26, grade=60)
obj1.display_info() 