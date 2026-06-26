#WAP to create ATM simulation.
balance = 1000.0 #Initialize account
pin = "1234"

print("---Mini ATM Simulation---")
user_pin = input("Enter PIN: ")

if user_pin == pin:
    while True:
        print("\n1.Balance 2.Deposit 3.Withdraw 4.Exit")
        choice = input("Choice: ")
        if choice == "1":
            print(f"Balance: ${balance: .2f}")
        elif choice == "2":
            balance += float(input("Deposit amount: $"))
        elif choice == "3":
            amt = float(input("Withdraw amount: $"))
            if amt <= balance: 
                balance -= amt
            else:
                print("Insufficient funds.")
        elif choice == "4":
            break
else:
    print("Invalid PIN")