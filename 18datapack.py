MENU ="""
1. Data Pack
2. Voice Pack
3. Day Pack
4. Unlimited Pack
5. Exit
"""
while True:
    print(MENU)
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Data Pack are:")
    elif choice==2:
        print ("Voice Pack are:")
    elif choice==3:
        print("Day pack are:")
    elif choice==4:
        print("Unlimited pack are:")
    elif choice==5:
        print("Thanks for using our service.")
        print("NCELL NEPAL")
        break
    else:
        print("Invalid Choice.")    
    
        