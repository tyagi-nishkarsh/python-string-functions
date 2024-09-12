#16. Write a Python program to count the number of vowels and consonants in a string.

vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

a = input("Enter a string: ")


for char in a:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")