# class Student:
#     def __init__ (self, name, grade):
#         self.name=name
#         self.grade=grade
#     def get_data(self):
#         return (f"name is{self.name} and grade is{self.grade}")
#     def is_passed(self):
#         if self.grade>35:
#             return True
#         else:
#             return False

# #object
# s1=Student(name="Jaya", grade=50)
# print(s1.get_data())

class Student:
    def __init__(self, name,age):
        self.name=name
        self.age=age
    
s1=Student(name="Jaya", age=26)
print(f"{s1.name} is {s1.age} years old.")
