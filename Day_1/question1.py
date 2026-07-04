#WAP to calculate sum of first N natural numbers.
n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a number greater than 0.")
else:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i

    print(f"The sum of the first {n} natural numbers is: {total_sum}")