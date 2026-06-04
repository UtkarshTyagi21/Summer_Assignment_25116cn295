#WAP to find LCM of two numbers
def LCM(a,b):
    greater = max(a,b)
    smallest = min(a,b)
    for i in range(greater,a*b+1,greater):
        if i % smallest == 0:
            return i

if __name__ == '__main__' :
    a = 12
    b = 15
    print("LCM of",a,"and",b,"is", LCM(a,b))