# Program to demonstrate bank software
class BankAccount():
    def __init__ (self, name, phone, balance=0.00):
        self.name = name
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Successful deposit of Rs.{amount:.2f} to {self.name}'s account.")
        else:
            print("Invalid Deposit Amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs.{amount:.2f} from {self.name}'s account.")
        else:
            print("Invalid Withdrawal Amount or Insufficient Balance")
    
    def get_amount(self):
        return f"{self.name}'s current balance: Rs.{self.balance:.2f}"

# Usage
Jaya = BankAccount("Jaya", "9867325246")
Jaya.deposit(17000)
Jaya.withdraw(5000)

print(Jaya.get_amount())

