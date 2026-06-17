#WAP to intersection of arrays.
def intersect_with_sets(arr1, arr2): #Converts lists to sets and fond common elements
    return list(set(arr1) & set(arr2)) 

#Example usage
array_a = [1,2,2,1,4,5]
array_b = [2,2,5,6]

result = intersect_with_sets(array_a, array_b)
print("Intersection : ", result) #Output: [2,5]

