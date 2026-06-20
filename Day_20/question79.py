#WAP to find row-wise sum.
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for i in range(len(matrix)): #Loop through each row index
    row_sum = 0
    for j in range(len(matrix[i])): #Loop through each column element in the current row
        row_sum += matrix[i][j]

    print("Sum of Row",(i + 1),":", row_sum)