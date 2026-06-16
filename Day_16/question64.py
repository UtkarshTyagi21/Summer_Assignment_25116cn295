#WAP to remove duplicates from array.
def remove_duplicates(input_array):
    seen = set()
    result = []

    for element in input_array:
        if element not in seen:
            result.append(element)
            seen.add(element)

    return result

arr = [1,3,5,3,7,1,9,5]
print("Unique (Loop): ", remove_duplicates(arr))