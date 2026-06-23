#WAP to find first repeating character.
def find_first_repeating_char(text):
    seen_characters = set() #Initialize an empty set to track characters we've already seen

    #Loop through each character in the string
    for char in text:
        if char in seen_characters: #If the character is already in our set,it is the first duplicate
            return char
        
        seen_characters.add(char) #Otherwise , add the character to the set and keep moving

    return None #Return None if all characters in the string are unique

#---Example Usage---
test_string_1 = "abcdefd"
test_string_2 = "python"
test_string_3 = "aba"

print("First repeating in ", test_string_1 , ":", find_first_repeating_char(test_string_1))
print("First repeating in ", test_string_2, ":" , find_first_repeating_char(test_string_2))
print("First repeating in ", test_string_3 , ":" , find_first_repeating_char(test_string_3))