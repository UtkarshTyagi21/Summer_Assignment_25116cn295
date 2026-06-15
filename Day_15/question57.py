#WAP to reverse array.
def reverse_array_manual(arr):
    start = 0
    end = len(arr) - 1

    while start < end : #Swap elements from outside in
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
    return arr

#Test the manual function
arr = [1,2,3,4,5]
print("Manually Reversed : ", reverse_array_manual(arr)) #Output : [5,4,3,2,1]