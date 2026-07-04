#WAP to print multiplication table of a given number.
num = int(input("Display multiplication table of ?"))

for i in range(1,11):
    print(num, 'X' , i , '=', num*i)