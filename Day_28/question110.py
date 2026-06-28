#WAP to create bank account system.
balance = 0

while True:
    choice = input("\n1. Balance | 2. Deposit | 3. Withdraw | 4. Exit\nChoice: ")

    if choice == '1':
        print(f"Current Balance: ${balance}")
    elif choice == '2':
        balance += float(input("Enter deposit amount: "))
        print("Successfully Deposited !")
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Success!")
        else:
            print("Insufficient funds!")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")

