#WAP to develop complete mini project using arrays, strings and functions.
# Contact Management System
# Arrays (Lists) to store data
names = []
phones = []

def add_contacts():
    """Adds a new contact name and phone number."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    if name and phone:
        names.append(name)
        phones.append(phone)
        print("Contact added successfully!")
    else:
        print("Invalid input. Name and phone cannot be empty.")

def view_contacts():
    """Display all stored contacts."""
    if not names:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for i in range(len(names)):
        print(f"{i+1}. Name: {names[i]} | Phone: {phones[i]}")

def search_contact():
    """Searches for a contact by name using string matching."""
    query = input("Enter name to search: ").strip().lower()
    found = False
    for i in range(len(names)):
        if query in names[i].lower():
            print(f"Found -> Name: {names[i]} | Phone: {phones[i]}")
            found = True
    if not found:
        print("No matching contact found.")

def main():
    """Main program loop to navigate the menu."""
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_contacts()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

#Run the project
if __name__ == "__main__":
    main()