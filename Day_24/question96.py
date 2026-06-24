#WAP to remove duplicate characters.
def remove_duplicate_loop(input_string):
    seen = set()
    result = []

    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return "".join(result)

#Example Usage
text = "hello world"
print(remove_duplicate_loop(text)) #Output: helo wrd