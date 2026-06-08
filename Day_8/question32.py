#WAP to print repeated-number pattern.
#1
#22
#333
#4444
#55555

rows = 6
for i in range(1,rows):
    for j in range(i):
        print(i,end="")
    print()