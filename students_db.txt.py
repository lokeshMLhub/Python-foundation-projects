def add_student():
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = input("Enter marks: ")

    with open("students_db_txt", "a") as f:
        f.write(f"{name},{branch},{marks}\n")
    print("Student saved successfully!")

def show_students():
    with open("students_db_txt", "r") as f:
          print("\n--- All Students ---")
          print(f.read())

while True:
    print("\n1. Add student")
    print("2. Show students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
        