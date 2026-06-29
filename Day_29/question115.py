#WAP to create menu-driven string operations system.
while True:
    print("\n--- STRING OPERATIONS MENU ---")
    print("1. Reverse the string")
    print("2. Change to Uppercase")
    print("3. Check the Length")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '4':
        print("Exiting the program. Goodbye !")
        break
    elif choice in ('1', '2' , '3' ):
        user_string = input("Enter your string: ")

        if choice == '1':
            reversed_str = user_string[::-1]
            print(f"Reversed String: {reversed_str}")

        elif choice == '2':
            print(f"Uppercase String: {user_string.upper()}")
        
        elif choice == '3':
            print(f"Length of String: {len(user_string)}")

    else:
        print("Invalid choice! Please pick a number from 1 to 4.")