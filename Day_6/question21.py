#WAP to convert decimal to binary.
n = int(input("Enter the number: "))
res = '' #Binary Result

while n > 0:
    res = str(n % 2) + res
    n //= 2
print(res)