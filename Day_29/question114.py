#WAp to create menu-driven array operations system.
l1 = []

while True:
    print("---MENU DRIVEN PROGRAM---")
    print("1. View current list")
    print("2. Add an item")
    print("3. Insert item at a specific location")
    print("4. Remove an item")
    print("5. Remove last item(or by index)")
    print("6. Search for an item")
    print("7. Arrange items in ascending order")
    print("8. Reverse the list")
    print("9. Find the largest & the smallest items")
    print("10. Count the frequency of an item")
    print("11. Clear the entire list")
    print("12. Exit the program")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("My list is: ", l1)
    elif choice == 2:
        num = eval(input("Enter the element: "))
        l1.append(num)
    elif choice == 3:
        num = eval(input("Enter the element: "))
        pos = int(input("Enter the index location: "))
        l1.insert(pos,num)
    elif choice == 4:
        num = eval(input("Enter the element: "))
        l1.remove(num)
    elif choice == 5:
        pos = int(input("Enter the index location: "))
        l1.pop(pos)
    elif choice == 6:
        num = eval(input("Enter the element: "))
        for i in l1:
            if i == num:
                print("Element found")
    elif choice == 7:
        l1.sort()
        print(l1)
    elif choice == 8:
        l1.reverse() #Permanently reversed
        #l1[::-1]
        print(l1)
    elif choice == 9:
        print("Maximum items is: ", max(l1))
        print("Minimum items is: ", min(l1))
    elif choice == 10:
        num = eval(input("Enter the element: "))
        print(l1.count(num))
    elif choice == 11:
        l1.clear()
        print(l1)
    elif choice == 12:
        break #exit(0)