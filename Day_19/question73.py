#WAP to add matrices.
X = [[1,2,3],
     [4,5,6]]
Y = [[7,8,9],
     [1,2,3]]

result = [[0,0,0], #Initialize a result matrix filled with zeroes
          [0,0,0]]

for i in range(len(X)): #Iterate through rows
    for j in range(len(X[0])): #Iterate through columns
        result[i][j] = X[i][j] + Y[i][j]

print("Result using Nested Loops:")
for row in result:
    print(row)