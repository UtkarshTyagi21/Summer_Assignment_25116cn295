#WAP to check perfect number.
n = int(input("Enter a number: "))
Sum = 0
for i in range(1,n):
    if n % i == 0 :
        Sum = Sum + i
if (Sum == n):
    print("The entered number is a perfect number.")
else :
    print("The entered number is not a perfect number.")

