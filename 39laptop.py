class Laptop:
    def __init__(self, id, name, ram):
        self.id=id
        self.name=name
        self.ram=ram
    
    def dispay_data(self):
        return f"Laptop id is {self.id}, name is {self.name} and RAM is {self.ram} GB."
    
l1=Laptop (id=1, name="Dell", ram=8)
l2=Laptop (id=2, name="Lenovo", ram=16)
l3=Laptop (id=3, name="Acer", ram=4)

print(l1.dispay_data())
print(l2.dispay_data())
print(l3.dispay_data())