#WAP to convert binary to decimal.
def binaryTodecimal(b):
    d , p = 0, 0
    while b:
        d += (b % 10) * (2**p)
        b //= 10
        p += 1
    print(d)

for num in [100, 101]:
    binaryTodecimal(num)