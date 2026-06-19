#WAP to subtract matrices.
matrix1 = [[10,20,30],
           [40,50,60]]
matrix2 = [[1,2,3],
           [4,5,6]]

rows = len(matrix1)
cols = len(matrix1[0])
result = [[0 for j in range(cols)] for i in range(rows) ]

for i in range(rows): #Iterate through each row and column to subtract elements
    for j in range(cols):
        result[i][j] = matrix1[i][j] - matrix2[i][j]

print("Resulting Matrix:")
for row in result:
    print(row)