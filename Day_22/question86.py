#WAP to count words in a sentence.
def count_words(sentence):
    words = sentence.split() #split() handles arbitary whitespace automatically
    return len(words)

#Example usage:
text = "Python is fun and very versatile."
total_words = count_words(text)
print("The sentence has ", total_words , "words.") #Output : The sentence has 6 words.
