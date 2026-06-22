#WAP to character frequency.
def get_char_frequency_loop(text):
    frequency_map = {}

    for char in text:
        frequency_map[char] = frequency_map.get(char,0) + 1

    return frequency_map

#Example Usage
input_str = "programming"
frequency = get_char_frequency_loop(input_str)
print(frequency)