#WAP to compress a string.
def string_comp(s):
    scomp = [s[0]]
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            scomp.extend([count, s[i]])
            count = 1

    scomp.append(count)

    res = ''.join(map(str, scomp))

    return res

#Driver Code
s = "aaabbccccccccddeeeeeeeeeee" #a3b2c8e11
c_string = string_comp(s)
if len(c_string) < len(s):
    print(c_string)
else:
    print(s)