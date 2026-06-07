#WAP to recursive fibonacci.
def fib (n, prev1 , prev2 ) :
    if n < 3 :
        return
    fn = prev1 + prev2
    prev2 = prev1
    prev1 = fn
    print(fn, end = " ")
    fib(n - 1, prev1 , prev2)
def print_fib(n) :
    if n < 1 : #When the number of terms is less than one
        print("Invalid number of terms")
    elif n == 1 :
        print(0)
    elif n == 2 :
        print("0 1")
    else :
        print("0 1", end = " ")
        fib(n, 1, 0)

if __name__ == "__main__" :
    n = int(input("Enter a number : "))
    print_fib(n)