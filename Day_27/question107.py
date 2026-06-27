#WAP to create salary management system.
employees = {}

while True:
    choice = input("\n1. Add Employee 2. View Payroll\n3. Exit\nChoose option: ")

    if choice == '1':
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        basic = float(input("Enter Basic Salary: "))

        #Auto-calculate allowances and net salary
        allowances = basic*0.20 #20% allowance
        tax = basic * 0.10 #10% tax deduction
        net_salary = basic + allowances - tax

        employees[emp_id] = {"Name": name, "Net Salary": net_salary}
        print(f"Success! {name}'s Net Salary is calculated as: ${net_salary:.2f}")

    elif choice == '2':
        if not employees:
            print("No records found.")
        for emp_id,data in employees.items():
            print(f"ID: {emp_id} | Name: {data['Name']} | Net Payroll: ${data['Net Salary']:.2f}")

    elif choice == '3':
        print("Exiting system.")
        break
    else:
        print("Invalid choice, try again.")