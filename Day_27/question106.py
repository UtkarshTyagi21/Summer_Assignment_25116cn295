#WAP to create employee management system.
employees = {} #Storage dictionary using Employee ID as the unique key

while True:
    print("\n---EMPLOYEE MANAGEMENT SYSTEM---")
    print("1. Add 2. View All 3. Update 4. Delete 5. Exit")
    choice = input("Enter choice (1-5): ")

    if choice == '1':
        emp_id = input("Enter ID: ")
        if emp_id in employees:
            print("Error: ID already exists!")
        else:
            employees[emp_id] = {
                "name": input("Enter Name: "),
                "role": input("Enter Role: "),
                "salary": input("Enter Salary: ")
            }
            print("Employee added successfully!")

    elif choice == '2':
        if not employees:
            print("No employee records found.")
        for emp_id, info in employees.items():
            print(f"ID: {emp_id} | Name: {info['name']} | Role: {info['role']} | Salary: ${info['salary']}")
    
    elif choice == '3':
        emp_id = input("Enter Employee ID to update: ")
        if emp_id in employees:
            print("Leave blank to keep current value.")
            name = input(f"New Name ({employees[emp_id['name']]}): ")
            role = input(f"New Role ({employees[emp_id['role']]}): ")
            salary = input(f"New Salary ({employees[emp_id['salary']]}): ")
            employees[emp_id] = {"name": name, "role": role, "salary": salary}
            print("Employee updated successfully!")
        else:
            print("Error: Employee ID not found.")

    elif choice == '4':
        emp_id = input("Enter Employee ID to delete: ")
        if employees.pop(emp_id, None):
            print("Employee removed successfully!")
        else:
            print("Error: Employee ID not found.")

    elif choice == '5':
        print("Existing system. Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1and 5.")
    
