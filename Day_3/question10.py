#WAP to print prime numbers in a range.
x,y = 2,7
result = []

for n in range(x,y+1):
    if n <= 1:
        continue
    is_prime = True #assume n is prime
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            is_prime = False #n is not prime
            break
        if is_prime :
            result.append(n) #add prime number
print(result if result else "No")