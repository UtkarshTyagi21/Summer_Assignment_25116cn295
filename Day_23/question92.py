#WAP to find maximum occuring character.
def find_max_char_dict(text):
    if not text:
        return None, 0
    
    frequency = {}

    for char in text: #Populate the frequency dictionary
        frequency[char] = frequency.get(char, 0) + 1

    max_char = max(frequency, key = frequency.get)
    count = frequency[max_char]

    return max_char, count

#Test the function
input_str = "Apple"
char, count = find_max_char_dict(input_str)
print("The maximum occuring charcter is ", char, "with a count of", count , ".")