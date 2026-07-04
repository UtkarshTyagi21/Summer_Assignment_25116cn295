#WAP to check whether a number is palindrome.
n = int(input("Enter number : "))
x = n
rev = 0

while x > 0:
    r = x % 10
    rev = rev * 10 + r
    x = x // 10

print("Reverse of given number is" , rev)

if rev == n:
    print(n , "is a Palindrome")
else:
    print(n, "is not a Palindrome")