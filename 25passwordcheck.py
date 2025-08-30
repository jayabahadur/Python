password=(input("Enter Password:"))
at_least_1_number= not password.isalpha()

if at_least_1_number:
    print("Strong Password")
else:
    print("Weak Password")