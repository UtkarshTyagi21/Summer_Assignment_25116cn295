#WAP to find largest and smallest element.
numbers = [23,5,89,43,57,68,100] #Initialise a list of numbers

largest = numbers[0] #Assume the first element is both the largest and smallest
smallest = numbers[0]

for num in numbers: #Iterate through the list to compare elements
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest element: ", largest)
print("Smallest element: ", smallest)