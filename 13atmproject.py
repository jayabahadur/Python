balance = 20000
print("Welcome to NIC ASIA Bank ATM")

while True:
    input_text="""
What do you want?
1. Check Balance
2. Deposite Amount
3. Withdraw Amout
4. Exit Process
:
"""
    user_input=int(input(input_text))

    if user_input==1:
        print(f"Your balanace is={balance}")

    elif user_input==2:
        amount=float(input("Enter balance to deposite="))
        balance+=amount
        print(f"Deposite Success. Your new balance is={balance}")

    elif user_input==3:
        amount=float(input("Enter balance to withdraw="))
        if balance>=amount:
            balance-=amount
            print(f"Withdraw Success. Your new balance is={balance}")
        else:
            print("Insufficient Balance")
    elif user_input==4:
        print("Thank your for using ATM.")
        print("NIC ASIA Bank.")
        break
    else:
        print("Invalid Choice")


