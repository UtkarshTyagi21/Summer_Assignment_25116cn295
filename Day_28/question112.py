#WAP to create contact management system.
contacts = {}

while True:
    choice = input("\n1. Add\n2. View\n3. Delete\n4. Exit: ")

    if choice == '1':
        name = input("Name: ")
        contacts[name] = input("Phone: ")
    elif choice == '2':
        for name,phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == '3':
        contacts.pop(input("Name to delete: "), print("Not found"))
    elif choice == '4':
        break