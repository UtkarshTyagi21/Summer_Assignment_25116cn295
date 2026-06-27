#WAP to create student record management system.
students = {}

while True:
    print("\n---Student Record Management---")
    choice = input("1. Add | 2. View All | 3. Delete | 4. Exit\nChoose an option (1-4): ")

    if choice == '1':
        roll = input("Enter Roll Number: ")
        if roll in students:
            print("Record already exists!")
        else:
            name = input("Enter Student Name: ")
            marks = input("Enter Total Marks: ")
            students[roll] = {"Name": name, "Marks": marks}
            print(f"Success: Record for {name} added!")

    elif choice == '2':
        if not students:
            print("No student record found.")
        else:
            print("\nRoll No | Name | Marks")
            for roll,info in students.items():
                print(f"{roll} \t| {info['Name']} \t | {info['Marks']} ")

    elif choice == '3':
        roll = input("Enter Roll Number to delete: ")
        if students.pop(roll, None):
            print(f"Success: Roll number {roll} removed.")
        else:
            print("Error: Record not found!")

    elif choice == '4':
        print("Exiting application. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1,2,3 or 4.")