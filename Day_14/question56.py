#WAP to find duplicates in array.
def find_duplicate(arr):
    seen = set()
    duplicates = set()

    for item in arr:
        if item in seen:
            duplicates.add(item)
        else :
            seen.add(item)

    return list(duplicates)

#Example usage:
nums = [2,4,3,2,7,8,2,3,1]
print("Duplicate elements: ", find_duplicate(nums)) #Output: [2,3]