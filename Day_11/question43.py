#WAP to write function to check prime.
def prime_num(num):
    for i in range(2,num):
        if(num % i == 0):
            print("Not a prime number")
            break
    else :
        print("Prime number")

prime_num(6)
            