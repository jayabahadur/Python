atm_user_id=20
atm_user_pin=2056

inputid=int(input("Enter user id="))
inputpin=int(input("Enter user pin="))

if inputid==atm_user_id and inputpin==atm_user_pin:
    print("Login Successful")
else:
    print("Login Failed")