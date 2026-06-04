#WAP to find nth Fibonacci term.
def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("Input must be a non-neagative integer.")
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a
n = int(input("Enter the term :"))
print("The",n,"th Fibonacci term is: ",fibonacci_iterative(n))