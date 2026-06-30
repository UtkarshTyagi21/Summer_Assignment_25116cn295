#WAP to create mini library system.
library = {"Python Basics": "Available", "Data Science 101": "Available"} #A simple dictionary representing the library collection.
#Format: "Book Title": "Availability Status"

while True:
    print("\n--- MINI LIBRARY SYSTEM ---")
    print("1. View Books\n2. Add Book\n3. Issue Book\n4. Return Book\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\nLibrary Collection: ")
        for book, status in library.items():
            print(f"- {book}: [{status}]")

    elif choice == "2":
        title = input("Enter book title to add: ").strip()
        if title:
            library[title] = "Available"
            print(f"'{title}' added successfully!")

    elif choice == "3":
        title = input("Enter book title to issue: ").strip()
        if library.get(title) == "Available":
            library[title] = "Issued"
            print(f"You have successfully issued '{title}'.")
        else:
            print("Book is either not available or does not exist.")

    elif choice == "4":
        title = input("Enter book title to return: ").strip()
        if library.get(title) == "Issued":
            library[title] = "Available"
            print(f"Thank you for returning '{title}'.")
        else:
            print("This book was not issued from this library.")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 5.")