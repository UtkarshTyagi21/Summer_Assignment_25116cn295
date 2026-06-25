#WAP to check string rotation.
def is_rotation(str1, str2):
    if len(str1) != len(str2) or not str1: #Check if lengths match and strings are not empty
        return False
    
    temp = str1 + str1 #Concatenate str1 with itself

    return str2 in temp #Check if str2 is a substring of the concatenated string

#---Test Cases---
string1 = "ABCD"
string2 = "CDAB"

if is_rotation(string1, string2):
    print(string2, "is a rotation of", string1)
else:
    print(string2 , "is NOT a rotation of", string1)