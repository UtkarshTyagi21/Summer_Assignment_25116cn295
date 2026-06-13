#WAP to count even and odd elements.
numbers = [1,2,3,4,5,6,7,8,9] #Define a list of numbers

even_count = 0 #Initialize counter variables
odd_count = 0

for num in numbers: #Iterate through each element in the list
    if num % 2 == 0:
        even_count += 1
    else :
        odd_count += 1

print("Total even elements : ", even_count)
print("Total odd elements : ", odd_count)