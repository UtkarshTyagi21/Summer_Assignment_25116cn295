#WAP to find GCD of two numbers.
a = 60 #first number
b = 48 #second number

#loop until the remainder is 0
while b != 0 :
    a, b = b, a % b

print(a)