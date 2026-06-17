#WAP to merge arrays.
array1 = [1,2,3]
array2 = [4,5,6]
merged_array = array1 + array2 #Approach A: Using the + operator (Creates a new list)
print("Merged with +: ", merged_array) #Output: [1,2,3,4,5,6]

array1.extend(array2) #Approach B: Using extend() (Modifies the first list in-place)
print("Merged with extend() : ",array1) #Output: [1,2,3,4,5,6]

arr_a = ['a' , 'b'] #Approach C: Using unpacking (Creates a new list)
arr_b = ['c' , 'd']
merged_unpack = [*arr_a , *arr_b]
print("Merged with unpacking: ", merged_unpack) #Output: ['a' , 'b' , 'c' , 'd']