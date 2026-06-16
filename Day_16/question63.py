#WAP to find pair with given sum.
def find_pair_with_sum(arr, target_sum):
    seen_numbers = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen_numbers:
            return (complement, num)
        seen_numbers.add(num)

    return None

#Example usage
numbers = [2,7,11,15,4,5]
target = 9
result = find_pair_with_sum(numbers, target)

if result:
    print("Pair found:", result)
else :
    print("No pair with the given sum exists.")