#WAP to calculate menu-driven calculator.
print("Enter two numbers")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
ch = 0

while ch < 5:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        sum = n1 + n2
        print("Sum = ", sum)
    elif ch == 2:
        diff = n1 - n2
        print("Difference = ", diff)
    elif ch == 3:
        mul = n1 * n2
        print("Product = ", mul)
    elif ch == 4:
        div = n1/n2
        print("Quotient = ", div)
    elif ch == 5:
        print("Thank you for using calculator.")
        break
    else:
        print("Invalid choice !")