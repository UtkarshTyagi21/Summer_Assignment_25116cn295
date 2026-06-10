#WAP to print number pyramid.
def print_number_pyramid(rows):
    for i in range(1, rows + 1): #Outer loop for each row.
        print(" " * (rows - i), end = "")  #Inner loop 1: Print leading spaces for alignment.
        for j in range(1, i + 1): #Inner loop 2: Print increasing numbers.
            print(j, end = "")
        for k in range(i - 1, 0, -1): #Inner loop 3: Print decreasing numbers.
            print(k, end = "")
        print() #Move to the next line after completing the row

#Define the height of the pyramid
pyramid_height = 5
print_number_pyramid(5)