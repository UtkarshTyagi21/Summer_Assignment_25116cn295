#WAP to find maximum frequency element.
def find_max_frequency_element(nums):
    if not nums: #Handle empty list case
        return None
    frequency_map = {} #Dictionary to store counts of each element

    max_element = nums[0] #Variables to track the most frequency element and its count
    max_frequency = 0

    for num in nums: #Step 1: Populate the frequency map
        frequency_map[num] = frequency_map.get(num, 0) + 1

        if frequency_map[num] > max_frequency:
            max_frequency = frequency_map[num]
            max_element = num

    return max_element, max_frequency

#Example usage :
nums = [1,2,3,1,4,1,3,2,1,3]
element, frequency = find_max_frequency_element(nums)

print("The maximum frequency element is: ", element)
print("It appears", frequency, "times.")