#WAP to create inventory management system.
inventory = {"apple": 50, "banana": 100, "orange": 30}

def view_inventory():
    print("\n--- Current Inventory ---")
    for item,qty in inventory.items():
        print(f"{item.capitalize()}: {qty}")

def update_inventory():
    item = input("Enter item name: ").lower()
    qty = int(input("Enter quantity (use negative to subtract): "))
    inventory[item] = inventory.get(item, 0) + qty
    print(f"Updated {item}. New balance: {inventory[item]}")

#Main program loop
while True:
    choice = input("\n[1] View [2] Update [3] Exit: ")
    if choice == "1":
        view_inventory()
    elif choice == "2":
        update_inventory()
    elif choice == "3":
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")