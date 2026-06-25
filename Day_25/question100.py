#WAP to sort words by length.
a = ["Python", "C", "Java", "JavaScript", "Go"]

def len_sort(s): #Custom function for sorting
    return len(s)

b = sorted(a, key = len_sort) #Sorting using custom function
print(b) #Output: ['C', 'Go', 'Java', 'Python', 'JavaScript']