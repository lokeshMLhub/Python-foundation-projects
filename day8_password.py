password = input("Enter password: ")

if len(password) < 6:
    print("Weak")
elif "@" in password or "#" in password:
    print("Strong")
else:
    print("Medium")