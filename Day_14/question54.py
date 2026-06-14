#WAP to #find frequency of an element.
def find_frequency(arr, target):
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count

if __name__ == "__main__":
    numbers = [2,4,6,8,4,2,4,9]
    target_element = 4

    result = find_frequency(numbers, target_element)
    print("The element",target_element,"occurs",result,"times.")
