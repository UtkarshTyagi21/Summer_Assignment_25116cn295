#WAP to find sum of digits of a number.
num = int(input("Enter a number: "))

n = abs(num) #Handle negative numbers
digit_sum = 0

while n > 0: #Loop until the number becomes 0
    digit = n % 10 #Extract the last digit
    digit_sum += digit #Add it to the total sum
    n = n // 10 #Remove the last digit

print(f"The sum of the digits is: {digit_sum}")