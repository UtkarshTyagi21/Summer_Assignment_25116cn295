#WAP to print reverse star pattern.
rows = 5
for i in range (rows + 1):
    for j in range (5,i, -1):
        print("*", end = "")
    print()