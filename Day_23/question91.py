#WAP to check anagram strings.
def is_anagram_dict(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2): #Anagrams must always have identical lengths
        return False
    
    count = {}

    for char in str1: #Increment character counts for the first string
        count[char] = count.get(char, 0) + 1

    for char in str2: #Decrement charcter counts for the second string
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]

    return len(count) == 0 #If the dictionary is empty, all frequencies match perfectly

#Test cases
print(is_anagram_dict("The Morse Code", "Here Come Dots")) #Output: True
