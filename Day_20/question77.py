#WAP to multiply matrices.
def multiply_matrices(A, B):
    rows_A = len(A) #Get dimensions
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B: #Rule check: Columns of A must equal Rows of B
        raise ValueError("Matrices cannot be multiplied due to incompatible dimensions.")
    
    result =[[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A): #Iterate through rows of A
        for j in range(cols_B): #Iterate through columns of B
            for k in range(cols_A): #Iterate through rows of B (or columns of A)
                result[i][j] += A[i][k] * B[k][j]

    return result

#Define two sample matrices (nested lists)
matrix_a = [[1,2],
            [3,4]]

matrix_b = [[5,6],
            [7,8]]

#Calculate and display the result
output = multiply_matrices(matrix_a, matrix_b)
print("Result using vanilla(Standard) Python:")
for row in output:
    print(row)