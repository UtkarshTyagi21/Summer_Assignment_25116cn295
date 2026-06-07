#WAP to recursive reverse number.
def rev_num(n) :
    if n < 10 :
        return n
    return str(n % 10) + str(rev_num(n // 10))

n = int(input("Enter a number: "))
print("Reverse number is: ",rev_num(n))