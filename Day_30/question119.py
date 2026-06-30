#WAP to create mini employee management system.
employees = {} #Mini Employee Management System

while True:
    print("\n--- EMPLOYEE SYSTEM ---")
    print("1. Add 2. View 3. Delete 4. Exit")
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print("Error: ID already exists!")
        else:
            name = input("Enter Name: ")
            role = input("Enter Role: ")
            salary = input("Enter Salary: ")
            employees[emp_id] = {"Name": name, "Role": role, "Salary": salary}
            print(f"Employee '{name}' adeded successfully!")

    elif choice == '2':
        if not employees:
            print("No records found.")
        else:
            for emp_id,info in employees.items():
                print(f"ID: {emp_id} | Name: {info['Name']} | Role: {info['Role']} | Salary: ${info['Salary']}")

    elif choice == "3":
        emp_id = input("Enter Employee ID to delete: ")
        if employees.pop(emp_id, None):
            print("Employee deleted successfully!")
        else:
            print("Error: Employee ID not found.")

    elif choice == "4":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1-4.")