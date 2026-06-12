#WAP to write function for perfect number.
def is_perfect_number(n):
    if n <= 1: #Perfect numbers must be greater than 1
        return False
    
    divisor_sum = 0 #Loop from 1 up to half of n (inclusive)
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisor_sum += i

    return divisor_sum == n #Return True if the sum equals the original number

#Test the function
test_num = 6
if is_perfect_number(test_num):
    print(test_num, "is a perfect number.")
else :
    print(test_num,"is not a perfect number.")