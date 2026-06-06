#WAP to find x^n without pow().
def power_optimized(x, n):
    if n < 0: #Handle negative exponents by inverting the base and making n positive
        x = 1/x
        n = -n

    result = 1
    current_product = x

    while n > 0:
        if n % 2 == 1: #If n is odd, multiply the result by current product
            result *= current_product
        current_product *= current_product #square the current product and halve the exponent
        n //= 2

    return result
#Example Usage
print(power_optimized(2.0, 10)) # Output: 1024.0
print(power_optimized(2.0, -2)) # Output: 0.25

