#WAP to union of arrays.
array1 = [1,2,2,3,4] #Two sample array (lists)
array2 = [3,4,5,6,6]

union_set = set(array1) | set(array2) #Find union using the set union operator '|'

union_list = list(union_set) #Convert back to a list

print("Union of arrays: ", union_list) #Output: [1,2,3,4,5,6]