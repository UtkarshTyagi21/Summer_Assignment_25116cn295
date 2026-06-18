#WAP to Bubble sort.
def bubble_sort(arr):
    n = len(arr)

    for i in range(n): #Outer loop to traverse through all array elements
        swapped = False #Track if any swap happens in this pass
#Inner loop for adjacent comparison
        for j in range(0, n - i - 1): #Last i elements are already in place, so we skip them

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        #If no two elements were swapped by inner loop, the list is sorted
        if not swapped:
            break

#Example usage
if __name__ == "__main__":
    data_list = [64,34,25,12,22,11,90]
    print("Original Array:", data_list)

    bubble_sort(data_list)
    print("Sorted Array: ", data_list)
