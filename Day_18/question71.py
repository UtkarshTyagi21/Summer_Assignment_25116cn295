#WAP to Bnary search.
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 #Calculate the middle index

        if arr[mid] == target: #Check if the target is at the mid position
            return mid
        elif arr[mid] < target: #If target is greater, ignore the left half
            left = mid + 1
        else: #If target is smaller, ignore the right half
            right = mid - 1

    return -1  #Return -1 if the element is not found

#Example Usage (The array MUST be sorted)
numbers = [2,5,8,12,16,23,38,56,72,91]
target_value = 23

result = binary_search(numbers , target_value)

if result != -1:
    print("Element found at index: ", result)
else:
    print("Element not found in the array")