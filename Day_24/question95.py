#WAP to find longest word.
def find_longest_word_loop(sentence):
    words = sentence.split()
    longest_word = ""

    for word in words: #Iterate through the array to check word lengths
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

#Example Usage
text = "Explore data science and machine learning"
print("The longest word is:", find_longest_word_loop(text))