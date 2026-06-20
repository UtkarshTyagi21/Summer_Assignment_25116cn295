#WAP to find column-wise sum.
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for j in range(len(matrix)): #Loop through each column index
    column_sum = 0
    for i in range(len(matrix[j])): #Loop through each row element in the current column
        column_sum += matrix[i][j]

    print("Sum of Column",(j + 1),":", column_sum)