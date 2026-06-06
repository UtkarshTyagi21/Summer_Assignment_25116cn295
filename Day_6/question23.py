#WAP to count set bits in number.
def countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count
i = int(input("Enter any number: "))
print(countSetBits(i))