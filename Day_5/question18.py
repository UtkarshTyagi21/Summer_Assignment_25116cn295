#WAP to check strong number.
def is_strong(num):
    temp = num
    sum_factorials = 0

    while temp > 0:
        digit = temp % 10 # Get the last digit

        fact = 1
        for i in range(1, digit+1): # factorial calculations
            fact *= i

        sum_factorials += fact # Add its factorial
        temp //= 10 #Remove last digit
    return sum_factorials == num # Compare with original number
# Test the value
number = 145
if is_strong(number):
    print(f"Given {number} is a Strong Number")
else:
    print(f"Given {number} is not a Strong Number")