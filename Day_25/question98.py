#WAP to find common characters in strings.
def find_unique_common_charts(str1, str2):
    set1 = set(str1) #Convert strings to sets to get unique characters
    set2 = set(str2)

    common = set1.intersection(set2) #Find the intersection between both sets

    return sorted(list(common)) #Return as a sorted list for clean output

#Example Usage
string1 = "apple"
string2 = "pineapple"
print("Unique common characters: ", find_unique_common_charts(string1, string2)) #Output: ['a', 'e', 'l', 'p']