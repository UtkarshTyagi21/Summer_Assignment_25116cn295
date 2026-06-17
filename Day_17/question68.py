#WAP to find common elements.
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

common_elements = list(set(list1) & set(list2)) #Method A: Using the & operator
print("Common elements (&) : ", common_elements)

common_elements_alt = list(set(list1).intersection(list2)) #Method B: Using the .intersection() method
print("Common elements (intersection) : ", common_elements_alt) #Output : [3,4,5]
