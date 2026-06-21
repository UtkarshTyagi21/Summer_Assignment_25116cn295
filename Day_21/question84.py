 #WAP to convert lowercase to uppercase.
def manual_uppercase(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z': #Check if the character is lowercase 
            result += chr(ord(char) - 32) #Subtract 32 to convert to uppercase
        else:
            result += char #Leave numbers, symbols, and uppercase letters unchanged
    return result

user_input = input("Enter a string: ")
print("Uppercase result: ", manual_uppercase(user_input))