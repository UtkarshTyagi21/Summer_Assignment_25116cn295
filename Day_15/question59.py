#WAP to rotate array right.
def reverse(arr,start,end): #Helper function to reverse elements in place.
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_right(arr,k): #Rotates the array right by k steps.
    n = len(arr)
    if n == 0:
        return
    
    k = k % n #Handle cases where k is greater than the array length

    reverse(arr,0,n-1) #Step 1: Reverse the entire array
    reverse(arr,0,k-1) #Step 2: Reverse the first k elements
    reverse(arr,k,n-1) #Step 3: Reverse the remaining n-k elements

#Example Usage :
nums = [1,2,3,4,5,6,7]
k = 3
rotate_right(nums,k)
print("Rotated Array: ", nums) #Output: [5,6,7,1,2,3,4]
