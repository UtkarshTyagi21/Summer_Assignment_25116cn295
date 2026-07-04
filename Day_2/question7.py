#WAP to find product of digits.
num = int(input("Enter the number = "))

mul = 1
while num > 0:
    digit = num % 10
    mul = mul * digit
    num //= 10
print("Multiplication of digits of the number is = ", mul)