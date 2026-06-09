#WAP to print repeated character pattern.
n = 5
for i in range(1, n + 1):
        char = chr(64 + i)  # ASCII: A=65, so 64+i gives correct letter
        print(char * i)     # Repeat the character i times