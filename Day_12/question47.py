#WAP to write function for Fibonacci.
def generate_fibonacci(n):
    """
 Generate a list containing the Fibonacci sequence up to n terms.
    """
    if n <= 0 :  #Handle edge case where no terms are requested
        return []
    elif n == 1: #Handle edge case for exactly one term.
        return [0]
    fib_sequence = [0, 1] #Start with the first two term of the sequence
    for i in range(2,n): #Calculate the remaining terms using a loop
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

#Example usage:
terms = 10
print("Fibonacci series for", terms, "terms: ")
print(generate_fibonacci(terms))