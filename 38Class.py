class Student:
    def __init__(self, name, age):
        self.name=name
        self.age= age
    
    def get_info(self):
        return f"Name is {self.name} and age is {self.age}"

s1=Student(name="Jaya", age=26)
print(s1.get_info())
