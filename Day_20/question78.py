#WAP to check symmetric matrix.
def is_symmetric(matrix):
    if not matrix or not matrix[0]: #Check if the matrix is empty
        return False
    
    rows = len(matrix)

    for row in matrix: #1. Validate if it is a square matrix
        if len(row) != rows:
            return False
        
    for i in range(rows): #2. Check for symmetry across the diagonal
        for j in range(i): #Only loops through elements below the diagonal
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

#---Verification---
symmetric_matrix = [[1,7,3],
                    [7,4,-5],
                    [3,-5,6]]

asymmetric_matrix = [[1,2,3],
                     [4,5,6],
                     [7,8,9]]

print("Symmetric test:", is_symmetric(symmetric_matrix)) #Output: True
print("Asymmetric test:", is_symmetric(asymmetric_matrix)) #Output: False