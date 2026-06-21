#WAP to count vowels and consonants.
def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    vowel_set ={'a','e','i','o','u'}

    for char in text.lower():
        if char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1

    print("Vowels : ", vowels)
    print("Consonants : ", consonants)

user_input = input("Enter a string: ")
count_vowels_consonants(user_input)