#WAP to print reverse pyramid.
rows = 5

for i in range(rows, 0 , -1):
    for j in range(rows - i): #Print spaces for alignment.
        print(" ", end = "")
    for k in range(2*i-1): #Print stars
        print("*", end = "")
    print() #Move to the next line
