#WAP to create student record system using arrays and strings.
names = [] #Array to store student names (Strings)
marks = [] #Array to store student marks (Numbers)

while True:
    choice = input("\n1. Add 2. Display 3. Search 4. Exit\nChoose option: ")

    if choice == "1":
        names.append(input("Enter student name: "))
        marks.append(input("Enter student marks: "))
        print("Record saved successfully!")

    elif choice == "2":
        if not names: print("No records found.")
        for i in range(len(names)):
            print(f"Name: {names[i]} | Marks: {marks[i]}")

    elif choice == "3":
        query = input("Enter name to search: ")
        if query in names:
            idx = names.index(query)
            print(f"Found! Name: {names[idx]} | Marks: {marks[idx]}")
        else:
            print("Student record not found.")

    elif choice == "4":
        print("Exiting system...")
        break
    else:
        print("Invalid choice! Try again.")