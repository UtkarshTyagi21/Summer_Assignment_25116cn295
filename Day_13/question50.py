#WAP to find sum and average of array.
arr = [10,20.30,40,50]

total_sum = 0
count = 0

for num in arr: 
    total_sum += num
    count += 1
if count > 0 :
    average = total_sum / count
else :
    0

print("Sum = ", total_sum)
print("Average =", average)
