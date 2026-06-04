#WAP to check Armstrong number.
num = int(input("Enter a number: ")) #Take input from the user
num_digits = len(str(num))  #Initialize sum and find the 
sum_of_powers = 0
temp = num #Use a temporary variable to preserve the  original number
while temp > 0:
    digit = temp % 10 #Extracts the last digit
    sum_of_powers += digit ** num_digits #Raise digit to power and adds to sum
    temp //= 10 #Removes the last digit
#Check if the sum matches the original number
if num == sum_of_powers:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number. ")