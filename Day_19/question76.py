#WAP to find diagonal sum.
def diagonal_sum(matrix):
    n = len(matrix)
    total_sum = 0

    for i in range(n):
        total_sum += matrix[i][i] #Add primary diagonal element

        total_sum += matrix[i][n - 1 - i] #Add secondary diagonal element

#If the matrix size is odd, subtact the centre element
#because it was added twice by both diagonals
    if n % 2 == 1:
        total_sum -= matrix[n // 2][n // 2]

    return total_sum

#Example Usage
matrix_example = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]

print("Total Diagonal Sum:", diagonal_sum(matrix_example)) #Output: 25(1 + 5 + 9 + 3 + 7)