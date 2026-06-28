#WAP to create library management system.
library = {"Python Basics": True, "Data Science 101": True, "AI for Beginners": True} #A Simple dictionary to stor book titles and their availability status (True = Available)

while True:
    choice = input("\n1. View Books\n2. Add Books\n3. Borrow Book\n4. Return Book\n5. Exit\nChoose (1-5): ")

    if choice == "1":
        for book, status in library.items():
            print(f"- {book} [{'Available' if status else 'Borrowed'}]")

    elif choice == "2":
        library[input("Enter book title to add: ")] = True
        print("Book added successfully!")

    elif choice == "3":
        title = input("Enter book title to borrow: ")
        if library.get(title) == True:
            library[title] = False
            print("You have borrowed the book.")
        else:
            print("Book is either unavilable or does not exist.")

    elif choice == "4":
        title = input("Enter book title to return: ")
        if title in library and not library[title]:
            library[title] = True
            print("Book returned successfully.")
        else:
            print("This book does not borrowed or doesn't belong here.")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")