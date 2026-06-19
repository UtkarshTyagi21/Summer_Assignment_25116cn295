#WAP to transpose matrix.
matrix = [[1,2],
          [3,4],
          [5,6]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))] #The outer loop determines the column index, inner loop pulls from rows

print(transposed) #Output: [[1,3,5], [2,4,6]]