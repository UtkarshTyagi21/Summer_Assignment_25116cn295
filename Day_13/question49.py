#WAP to input and display array.
n = int(input("Enter the number of elements: ")) #1. Take the number of elements from the user
user_array = [] #Initialize an empty list
print("Enter",n,"elements: ") #2. Input array elemnts using a loop
for i in range(n):
    element = int(input("Element " + str(i + 1) + ": "))
    user_array.append(element)

print("\nThe entered array is:",user_array) #3. Display the array
