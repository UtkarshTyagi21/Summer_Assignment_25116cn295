#WAP to find missing number in array.
def find_missing_number(arr):
    n = len(arr) + 1 #N is the total count of numbers including the missing one
    expected_sum = (n*(n + 1)) // 2 #Sum of numbers from 1 to N
    actual_sum = sum(arr) #Sum of elements present in the array
    return expected_sum - actual_sum #The difference is the missing number

#Example usage
nums = [1,2,4,5,6] #3 is missing
print("Missing number: ", find_missing_number(nums))