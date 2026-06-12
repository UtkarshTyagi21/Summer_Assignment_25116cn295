#WAP write function for armstrong.
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
def armstrong_recursive(n, num_digits):
    if n == 0:
        return 0
    return (n %10)**num_digits + armstrong_recursive(n // 10, num_digits)
def is_armstrong(n):
    num_digits = count_digits(n)
    armstrong_sum = armstrong_recursive(n, num_digits)
    return armstrong_sum == n
num = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number .")
else :
    print(num , "is not an Armstrong number .")