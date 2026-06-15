#WAP to rotate array left.
def reverse_subarray(arr,start,end):
    while start < end:
        arr[start], arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
def left_rotate(arr,d):
    n = len(arr)
    if n == 0:
        return arr
    
    d = d % n #Handle cases where d is greater than array length

    reverse_subarray(arr,0,d-1) #Step 1: Reverse first d elements
    reverse_subarray(arr,d,n-1) #Step 2: Reverse remaining elements
    reverse_subarray(arr,0,n-1) #Step 3: Reverse the whole array
    return arr

#Example Usage:
nums = [1,2,3,4,5,6,7]
print(left_rotate(nums, 2)) #Output: [3,4,5,6,7,1,2]