#WAP to check palindrome string.
def is_palindrome(s):
    s = s.lower() #Standardize to lowercase to handle mixed cases
    return s == s[::-1]

#Test the program
string = input("Enter a string: ")
if is_palindrome(string):
    print("Entered string is a palindrome")
else :
    print("Entered string is not a palindrome")