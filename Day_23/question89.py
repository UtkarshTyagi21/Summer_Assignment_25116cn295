#WAP to find first non-repeating character.
def first_non_repeating_char(s):
    char_count = {} #Step 1: Build the frequency map
    for char in s:
        char_count[char] =char_count.get(char , 0) + 1

    #Step 2: Find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char
     # Return None (or -1) if all characters repeat
    return None

#Driver Code
test_str = "swiss"
result = first_non_repeating_char(test_str)

print("The first non repeating character in",test_str,"is: ", result) #Output: The first non repeating character in 'swiss' is: w