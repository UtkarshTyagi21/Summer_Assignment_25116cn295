#WAP to find second largest element.
def get_second_largest(arr):
    if len(arr) < 2 : #There must be at least two elements
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest :
            second_largest = num
    return second_largest if second_largest != float('-inf') else None

#Example usage:
nums = [12,35,1,10,34,1]
result = get_second_largest(nums)
print("The second largest element is : ",result)